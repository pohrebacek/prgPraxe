<?php
namespace App\Module\Model\Post;

use App\Module\Model\Post\PostMapper;
use Nette;
use App\Module\Model\Post\PostsRepository;
use App\Module\Model\ExternalPost\ExternalPostsRepository;
use App\Module\Model\Comment\CommentsRepository;
use App\Module\Model\Post\PostDTO;
use App\Module\Model\User\UsersRepository;
use App\Module\Model\User\UserFacade;
use App\Module\Model\Like\LikesRepository;
use App\Module\Model\Comment\CommentFacade;
use App\Module\Model\ExternalPost\ExternalPostDTO;

final class PostFacade  //facade je komplexnější práci s nějakym repository, prostě složitější akce, plus může pracovat s víc repos najednou
{
	public function __construct(
		private PostsRepository $postsRepository,
		private CommentsRepository $commentsRepository,
        protected Nette\Database\Explorer $database,
        private PostMapper $postMapper,
        private UsersRepository $usersRepository,
        private LikesRepository $likesRepository,
        private CommentFacade $commentFacade,
        private ExternalPostsRepository $externalPostsRepository
	) {
	}

    public function filterPostColumns($data)
    {
        //funkce na filtraci dat z posts db na něco uživatelsky přívětívého
        foreach($data as $index => $line){
            $lineData = $line->toArray();
            foreach($lineData as $column => $value) {
                if ($column == "user_id") {
                    //$data[$column] = "Napsáno uživatelem: ";
                    //$data[$value] = ($this->usersRepository->getRowById($value))->username;
                    $lineData["Od uživatele: "] = ($this->usersRepository->getRowById($value))->username;
                }
                //bdump("$column, $value");
            }
            $data[$index] = $lineData;
        }         
        //bdump($data);
        return $data;
    }

    public function getPreview(PostDTO $post, int $previewCharacters): string {
        return substr($post->content, 0, $previewCharacters);
    }

    public function getOwnerUserName(PostDTO $post)
    {
        return $this->usersRepository->getUsernameById($post->user_id);
    }

    public function getPostsByFilter(string $column, $parameter)
    {
        if ($column == "id" && $parameter) {
            return $this->database->table($this->postsRepository->getTable())->where($column, $parameter)->fetchAll();
        }

        if ($column == "user_id" && $parameter) //parameter je jméno a ne id, uživateli se totiž bude líp hledat podle jména a ne podle id
        {
            $users = $this->database->table($this->usersRepository->getTable())->where("username LIKE ?", "%$parameter%")->fetchPairs("id", "username"); //vrátí pole ve tvaru id => username
            bdump($users);

            if (!$users) {
                return [];
            }
            
            return $this->database->table($this->postsRepository->getTable())->where($column . " IN ?", array_keys($users))->fetchAll();    //není potřeba žádnej foreach protože to obstarává samotnej dotaz
            
        }
        return $this->database->table($this->postsRepository->getTable())->where("{$column} LIKE ?", "%$parameter%")->fetchAll();   //i když dostane prázdnej string tak to vrátí všechno, protože LIKE vrací záznamy co obsahujou někde to cos zadal, proto u samotnáho WHERE to s "" vyhodí nic, protože se ptáš "vyhoď řádek co má v danym sloupci jenom hodnotu nic"
    }

    public function getNumberOfLikes(int $id)
    {
        return sizeof($this->likesRepository->getRowsByPostId($id));
    }

    public function deletePost(int $id): void
    {
        $this->database->transaction(function () use ($id) {
            $this->commentFacade->deleteComment($id);
            $this->externalPostsRepository->deleteExternalPostByPostId($id);
            $this->postsRepository->deleteRow($id);
        });
    }

    public function getPostDTO(int $id): PostDTO    //jedna funkce co za tebe převede row na DTO aniž bys to v kodu musel vypisovat jak kokot 
    {
        $postRow = $this->postsRepository->getRowById($id);
        return $this->postMapper->map($postRow);
    }

    public function countByUserAndMonth($userId, $date)
    {
        $start = new \DateTimeImmutable("{$date}-01 00:00:00"); //$date je ve formátu "YYYY-MM" ta tohle tomu přidá první den měsíce o půlnoci
        $end = $start->modify("first day of next month")->modify("-1 second");
        $countedPosts = sizeof($this->database->table($this->postsRepository->getTable())
            ->where("user_id = ?", $userId)
            ->where("created_at >= ?", $start)
            ->where("created_at <= ?", $end)
            ->fetchAll());
        return $countedPosts;
    }

    public function countByUserAndYear($userId, $year)
    {
        return sizeof($this->database->table($this->postsRepository->getTable())
            ->where("user_id", $userId)
            ->where("YEAR(created_at)", strval($year))
            ->fetchAll());
    }

    public function getOdlestPost($userId)
    {
        return $this->database->table($this->postsRepository->getTable())
            ->where("user_id", $userId)
            ->order("created_at DESC")
            ->fetch();
    }

    public function sortPosts(array $posts, string $sort)
    {
        bdump($sort);
        if ($sort == "DESC") {
            usort($posts, function($a, $b) {
                return strtotime($b->created_at) - strtotime($a->created_at);
            });
        }

        return $posts;
    }

    public function getImagePath(PostDTO $post)
    {
        if ($post->image){
			return $post->image;
		}
        return null;
    }


}

<?php
namespace App\Module\Model\Post;

use Nette;
use Nette\Database\Table\ActiveRow;
use App\Module\Model\Post\PostDTO;

class PostMapper {
    public function __construct(
    ) {}

    public function map(ActiveRow $row): PostDTO {
        return new PostDTO($row->id, $row->title, $row->content, $row->image, $row->user_id);
    }
}
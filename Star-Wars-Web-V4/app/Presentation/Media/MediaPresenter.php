<?php

namespace App\Presentation\Media;

use App\Model\Media\CanonStatus;
use App\Model\Media\MediaType;
use App\Model\Media\MediaRepository;
use App\Model\Media\MediaStatus;
use App\Model\Media\MediaFacade;
use App\Model\Era\EraFacade;
use App\Model\Era\ErasRepository;
use App\Presentation\Base\BasePresenter;
use Nette;
use Nette\Application\UI\Form;
use Nette\Utils\ArrayHash;

final class MediaPresenter extends BasePresenter
{
    public function __construct(
        private EraFacade $eraFacade,
        private MediaRepository $mediaRepository,
        private ErasRepository $erasRepository,
        private MediaFacade $mediaFacade,
    ) {}

    public function renderAdd():void
    {

    }

    public function actionDeleteMedia(int $mediaId): void
    {
        $this->mediaRepository->deleteRow($mediaId);
        $this->flashMessage('Dílo smazáno', 'success');
        $this->redirect('Timeline:show');
    }

    public function renderEdit(int $id): void
    {
        $media = $this->mediaFacade->getMediaDTO($id);

        if (!$media) {
            $this->error();
        }

        $this->getComponent('addForm')->setDefaults([
            'title' => $media->title,
            'description' => $media->description,
            'canon_status' => $media->canonStatus,
            'media_type' => $media->mediaType,
            'start_year' => $media->startYear,
            'end_year' => $media->endYear,
            'media_id' => $this->mediaFacade->getReferenceMediaId($media->id),
            'era_id' => $media->eraId,
            'part_label' => $media->partLabel,
            'release_date' => $media->releaseDate,
            'old_image_url' => $media->imageUrl,
        ]);
    }

    protected function createComponentAddForm(): Form
    {
        $form = new Form();

        $form->addText('title', "Název díla: ")
            ->setRequired('Vyplň název díla!')
            ->setHtmlAttribute('class', 'form-control');
        $form->addTextArea('description', "Popis (nepovinné, max 255 znaků): ")
            ->setHtmlAttribute('maxlength', 255)
            ->addRule($form::MaxLength, 'Maximálně 255 znaků.', 255);
        $form->addSelect("canon_status", "Zvol canon/legends", array_combine(
            array_map(fn($s) => $s->value, CanonStatus::forAdd()),
            array_map(fn($s) => $s->label(), CanonStatus::forAdd())
            ))
            ->setRequired("Vyber canon status")
            ->setHtmlAttribute('class', 'form-control');
        $form->addSelect("media_type", "Zvol typ díla", array_combine(
            array_map(fn($s) => $s->value, MediaType::forAdd()),
            array_map(fn($s) => $s->label(), MediaType::forAdd())
            ))
            ->setRequired("Vyber typ díla")
            ->setHtmlAttribute('class', 'form-control');
        $form->addInteger('start_year', 'Zadej v jakém SW roce dílo začíná (BBY => záporné číslo, ABY => kladné číslo')
            ->setRequired('Zadej počáteční rok díla')
            ->setHtmlAttribute('class', 'form-control');
        $form->addInteger('end_year', 'Zadej v jakém SW roce dílo končí (BBY => záporné číslo, ABY => kladné číslo')
            ->setRequired('Zadej konečný rok díla')
            ->setHtmlAttribute('class', 'form-control');
        $form->addSelect('media_id', 'Vyber po kterém díle se tvé dílo odehrává', (array) $this->mediaFacade->getAllMediaDTOsForForm() )
            ->setPrompt('--- Přidat na začátek ---')
            ->setHtmlAttribute('class', 'form-control');
        $form->addSelect('era_id', 'Vyber éru, do které dílo spadá: ', (array) $this->eraFacade->getAllErasForForm())
            ->setRequired('Vyber éru díla')
            ->setHtmlAttribute('class', 'form-control');
        $form->addText('part_label', 'Zadej část díla (nepovinné): ')
            ->setHtmlAttribute('class', 'form-control');
        $form->addDate('release_date', 'Datum vydání: ')
            ->setHtmlAttribute('class', 'form-control')
            ->setHtmlAttribute('min', date('Y-m-d'));
        $form->addUpload('image_url', 'Vyber obrázek: ')
            ->setHtmlAttribute('class', 'form-control')
            ->addRule(function ($item) {
                $mimeType = mime_content_type($item->getValue()->getTemporaryFile());
                return in_array($mimeType, ['image/jpeg', 'image/png', 'image/gif']);
            }, 'Soubor musí být platný obrázek (JPG/PNG/GIF).');
        $form->addHidden('old_image_url');
        $form->addSubmit('send', 'Potvrdit')
            ->setAttribute('class', 'btn btn-primary');

        $form->onSuccess[] = [$this, 'addFormSucceeded'];
        return $form;
    }

    private function getImageFromUrlForm(): ?string
    {
        if(isset($_FILES["image_url"]) && $_FILES["image_url"]["error"] == UPLOAD_ERR_OK){
            $tempPath = $_FILES["image_url"]["tmp_name"];

            $uploadDir = './images';
            $targetFile = $uploadDir . '/' .basename($_FILES["image_url"]["name"]);

            if (!file_exists($targetFile)) {
                move_uploaded_file($tempPath, $targetFile);
                bdump($tempPath);
            }
            return "http://www.localhost:8000/images/" . basename($_FILES['image_url']['name']);
        } else {
            return null;
        }
    }

    public function addFormSucceeded(Form $form): void
    {
        try {
            $formData = $form->getValues();
            bdump($formData);

            /*user si bude moct jen vybrat dílo PO KTERÉM se to nové odehrává, program sám dopočíta timline_order
            (pokud po tom díle něco je tak se tomu novému přidá timeline order jako průměr těch dvou,
            pokud po něm nic neni tak se timelien_order přiřadí jako prostě vyšší hodnota,
            a pokud user nic nezadá tak se nové dílo dá na začátek) tím by se mělo předejít zmatku a chaosu jak v kodu tak v ui
            */

            $data = ArrayHash::from([
                'title' => $formData['title'],
                'description' => $formData['description'],
                'canon_status' => $formData['canon_status'],
                'media_type' => $formData['media_type'],
                'start_year' => $formData['start_year'],
                'end_year' => $formData['end_year'],
                'era_id' => $formData['era_id'],
                'part_label' => $formData['part_label'],
                'timeline_order' => $this->mediaFacade->calculateTimelineOrder($formData['media_id']),
                'release_date' => $formData['release_date'],
                'image_url' => ($this->getImageFromUrlForm() == $formData['old_image_url'] || !$this->getImageFromUrlForm()) ? $formData['old_image_url'] : $this->getImageFromUrlForm(),
                'status' => MediaStatus::PLANNED->value
            ]);

            bdump($data);


            $media = $this->getParameter('id') ? $this->mediaRepository->saveRow((array) $data, $this->getParameter('id')) : $this->mediaRepository->saveRow((array) $data, null);
            if ($media) {
                $this->flashMessage('Akce proběhla úspěšně', 'success');
                $this->redirect('Timeline:show');
            }
            $this->flashMessage('Něco se pokazilo', 'danger');
            $this->redirect('Timeline:show');
        } catch (Nette\Database\DriverException $e) {
            $this->flashMessage('Použij normální znaky', 'danger');
        }
    }

}
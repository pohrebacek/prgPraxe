<?php

namespace App\Presentation\Timeline;

use App\Model\Media\MediaStatus;
use App\Presentation\Base\BasePresenter;
use App\Model\Media\MediaFacade;
use Nette;

final class TimelinePresenter extends BasePresenter
{
    public function __construct(
        private MediaFacade $mediaFacade
    ) {}
    public function renderShow(): void
    {
        $this->template->mediaDTOs = $this->mediaFacade->getAllMediaDTOs();
        $this->template->statusArray = array_combine(
            array_map(fn($s) => $s->value, MediaStatus::forStatusSelect()),
            array_map(fn($s) => $s->label(), MediaStatus::forStatusSelect())
        );
        bdump(array_combine(
            array_map(fn($s) => $s->value, MediaStatus::forStatusSelect()),
            array_map(fn($s) => $s->label(), MediaStatus::forStatusSelect())
        ));
    }

}
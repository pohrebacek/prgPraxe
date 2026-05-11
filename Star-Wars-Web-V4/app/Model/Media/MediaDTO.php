<?php

namespace App\Model\Media;

use Nette\Utils\DateTime;

readonly class MediaDTO
{
    function __construct(
        public int $id,
        public string $title,
        public ?string $description,
        public CanonStatus $canonStatus,
        public MediaType $mediaType,
        public int $startYear,
        public int $endYear,
        public int $eraId,
        public ?string $partLabel,
        public string $timelineOrder,
        public ?DateTime $releaseDate,
        public ?string $imageUrl,
        public MediaStatus $status,
    ) {}

    public function __ToString(): string
    {
        if ($this->partLabel) {
            return $this->title . ': ' . $this->partLabel;
        }
        return $this->title;
    }

    public function getFormattedYear(): string
    {
        if ($this->startYear == $this->endYear) {
            return $this->startYear < 0 ? abs($this->startYear) . ' BBY' : $this->startYear . ' ABY';
        }
        return
            ($this->startYear < 0 ? abs($this->startYear) . ' BBY - ' : $this->startYear . ' ABY - ')
            . ($this->endYear < 0 ? abs($this->endYear) . ' BBY' : $this->endYear . ' ABY');
    }
}
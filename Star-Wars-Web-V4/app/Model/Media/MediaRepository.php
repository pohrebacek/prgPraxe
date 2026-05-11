<?php

namespace App\Model\Media;

use App\Model\Base\BaseRepository;
use Nette;
use Nette\Database\Table\ActiveRow;

final class MediaRepository extends BaseRepository
{
    public function __construct(
        protected Nette\Database\Explorer $database,
    ) {
        $this->tableName = 'media';
    }

    public function getAllByTimelineOrder(): array
    {
        return $this->database->table($this->tableName)->order('timeline_order ASC')->fetchAll();
    }

    public function getFirstByTimelineOrder(): ?ActiveRow
    {
        return $this->database->table($this->tableName)->order('timeline_order ASC')->fetch();
    }

    public function getNextByTimelineOrder(ActiveRow $row): ?ActiveRow
    {
        return $this->database->table($this->tableName)->order('timeline_order ASC')->where('timeline_order >?', $row->timeline_order)->fetch();
    }

    public function getSomeByTimelineOrder(int $limit): ?ActiveRow
    {
        return $this->database->table($this->tableName)->order('timeline_order ASC')->limit($limit)->fetchAll();
    }

    public function getRowByTitle(string $title): ?ActiveRow
    {
        return $this->database->table($this->tableName)->where('title', $title)->fetch();
    }

    public function getRowByTitleAndLabel(string $title, string $label): ?ActiveRow
    {
        return $this->database->table($this->tableName)->where('title', $title)->where('part_label', $label)->fetch();
    }
}
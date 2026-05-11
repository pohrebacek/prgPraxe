<?php

namespace App\Model\Era;

use App\Model\Base\BaseRepository;

final class ErasRepository extends BaseRepository
{
    public function __construct(
        protected \Nette\Database\Explorer $database
    ) {
        $this->tableName = "eras";
    }

    public function getEraIdByName(string $era): ?int
    {
        $row = $this->database->table($this->tableName)->where("era_name", $era)->fetch();
        return $row ? (int)$row->era_id : null;
    }
}
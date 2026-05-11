<?php

namespace App\Model\Base;

use App\Model\Era\EraDTO;
use Nette;
use Nette\Database\Table\ActiveRow;

class BaseRepository
{
    protected string $tableName;
    public function __construct(
       protected Nette\Database\Explorer $database,
    ) {}

    public function getTableName(): string
    {
        return $this->tableName;
    }

    public function getRowById(int $id): ActiveRow|null
    {
        $row = $this->database->table($this->tableName)->get($id);
        if ($row instanceof ActiveRow) {
            return $row;
        }
        return null;
    }

    public function getAll(): array
    {
        return $this->database->table($this->tableName)->fetchAll();
    }

    public function deleteRow(int $id): int|null
    {
        $row = $this->getRowById($id);
        if($row instanceof ActiveRow) {
            return $row->delete();
        }
        return null;
    }

    public function saveRow(array $data, ?int $id): ActiveRow|null
    {
        if (!$id || !$this->getRowById($id)) {
            $row = $this->database->table($this->tableName)->insert($data);
            if ($row instanceof ActiveRow) {
                return $row;
            }
            return null;
        } else {
            $this->getRowById($id)->update($data);
            return $this->getRowById($id);
        }
        return null;
    }
}
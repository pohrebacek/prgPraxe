<?php

namespace App\Model\Era;

use Nette\Database\Table\ActiveRow;

class EraMapper
{
    function __construct(){}

    public function map(ActiveRow $row): EraDTO
    {
        return new EraDTO(
            $row->id,
            $row->era_name
        );
    }
}
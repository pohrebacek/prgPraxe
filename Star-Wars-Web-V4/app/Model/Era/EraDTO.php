<?php

namespace App\Model\Era;

readonly class EraDTO
{
    function __construct(
      public int $id,
      public int $eraName
    ){}
}
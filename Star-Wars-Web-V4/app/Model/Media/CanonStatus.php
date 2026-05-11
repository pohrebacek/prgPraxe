<?php

namespace App\Model\Media;

enum CanonStatus: string
{
    case LEGENDS = "legends";
    case CANON = "canon";

    public function label(): string
    {
        return match($this)
        {
            self::LEGENDS => "legends",
            self::CANON => "canon",
        };
    }

    public static function forAdd(): array
    {
        return [
            self::LEGENDS,
            self::CANON,
        ];
    }
}

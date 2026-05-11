<?php

namespace App\Model\Media;

enum MediaType: string
{
    case MOVIE = "movie";
    case SERIES = "series";
    case GAME = "game";
    case BOOK = "book";
    case COMIC = "comic";

    public function label(): string
    {
        return match($this)
        {
            self::MOVIE => "movie",
            self::SERIES => "series",
            self::GAME => "game",
            self::BOOK => "book",
            self::COMIC => "comic",
        };
    }

    public static function forAdd(): array
    {
        return [
            self::MOVIE,
            self::SERIES,
            self::GAME,
            self::BOOK,
            self::COMIC,
        ];
    }
}

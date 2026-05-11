<?php

namespace App\Model\Media;

enum MediaStatus: string
{
    case PLANNED = "planned";
    case IN_PROGRESS = "in_progress";
    case COMPLETED = "completed";
    case ON_HOLD = "on_hold";
    case DROPPED = "dropped";
    case REVISITING = "revisiting";

    public function label(): string
    {
        return match ($this) {
            self::PLANNED => "planned",
            self::IN_PROGRESS => "in_progress",
            self::COMPLETED => "completed",
            self::ON_HOLD => "on_hold",
            self::DROPPED => "dropped",
            self::REVISITING => "revisiting",
        };
    }

    public static function forStatusSelect(): array
    {
        return [
            self::PLANNED,
            self::IN_PROGRESS,
            self::COMPLETED,
            self::ON_HOLD,
            self::DROPPED,
            self::REVISITING,
        ];
    }
}

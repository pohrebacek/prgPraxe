<?php

namespace App\Model\Media;
use Nette\Database\Table\ActiveRow;

class MediaMapper
{
    function __construct(){}

    public function map(ActiveRow $row): MediaDTO {
        return new MediaDTO(
            $row->id,
            $row->title,
            $row->description,
            CanonStatus::from($row['canon_status']),
            MediaType::from($row['media_type']),
            $row->start_year,
            $row->end_year,
            $row->era_id,
            $row->part_label,
            $row->timeline_order,
            $row->release_date,
            $row->image_url,
            MediaStatus::from($row['status']),
        );
    }
}
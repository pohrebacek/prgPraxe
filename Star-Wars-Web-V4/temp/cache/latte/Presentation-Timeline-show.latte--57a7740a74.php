<?php

declare(strict_types=1);

use Latte\Runtime as LR;

/** source: C:\Users\Honza\PhpstormProjects\Star-Wars-Web-V4\Star-Wars-Web-V4\app\Presentation\Timeline/show.latte */
final class Template_57a7740a74 extends Latte\Runtime\Template
{
	public const Source = 'C:\\Users\\Honza\\PhpstormProjects\\Star-Wars-Web-V4\\Star-Wars-Web-V4\\app\\Presentation\\Timeline/show.latte';

	public const Blocks = [
		['content' => 'blockContent'],
	];


	public function main(array $ʟ_args): void
	{
		extract($ʟ_args);
		unset($ʟ_args);

		if ($this->global->snippetDriver?->renderSnippets($this->blocks[self::LayerSnippet], $this->params)) {
			return;
		}

		$this->renderBlock('content', get_defined_vars()) /* line 1 */;
	}


	public function prepare(): array
	{
		extract($this->params);

		if (!$this->getReferringTemplate() || $this->getReferenceType() === 'extends') {
			foreach (array_intersect_key(['mediaDTO' => '14', 'statusValue' => '37', 'statusLabel' => '37'], $this->params) as $ʟ_v => $ʟ_l) {
				trigger_error("Variable \$$ʟ_v overwritten in foreach on line $ʟ_l");
			}
		}
		return get_defined_vars();
	}


	/** {block content} on line 1 */
	public function blockContent(array $ʟ_args): void
	{
		extract($this->params);
		extract($ʟ_args);
		unset($ʟ_args);

		echo '<div class="navig">
    <a href="#The Old Republic" class="btn btn-primary">The Old Republic</a>
    <a href="#High Republic" class="btn btn-primary">High Republic</a>
    <a href="#Prequel Era" class="btn btn-primary">Prequel Era</a>
    <a href="#Galactic Empire Era" class="btn btn-primary">Galactic Empire Era</a>
    <a href="#New Republic Era" class="btn btn-primary">New Republic Era</a>
    <a href="';
		echo LR\Filters::escapeHtmlAttr($this->global->uiControl->link('Media:add')) /* line 8 */;
		echo '" class="btn btn-light">Add media</a>
</div>
<div>
    
</div>

';
		foreach ($mediaDTOs as $mediaDTO) /* line 14 */ {
			echo '<div class="container2">
    <div class="container" id="';
			echo LR\Filters::escapeHtmlAttr($eras[$mediaDTO->eraId]) /* line 15 */;
			echo '">
        <div class="imageAYear">
            <img src="';
			echo LR\Filters::escapeHtmlAttr(LR\Filters::safeUrl($mediaDTO->imageUrl)) /* line 17 */;
			echo '" class="image">
            <div>
                <p class="Year">';
			echo LR\Filters::escapeHtmlText($mediaDTO->getFormattedYear()) /* line 19 */;
			echo '</p>
                <p class="Status">';
			echo LR\Filters::escapeHtmlText($mediaDTO->canonStatus->value) /* line 20 */;
			echo '</p>
            </div>

        </div>

        <div class="nadpisAText">
            <h1>';
			echo LR\Filters::escapeHtmlText($mediaDTO->title) /* line 26 */;
			echo '</h1>
            <h3>';
			echo LR\Filters::escapeHtmlText($mediaDTO->partLabel) /* line 27 */;
			echo '</h3>
            <div class="line"></div>
            <p>';
			echo LR\Filters::escapeHtmlText($mediaDTO->description) /* line 29 */;
			echo '</p>
            <div class="line2"></div>
            <div class="stav">
                <a href="';
			echo LR\Filters::escapeHtmlAttr($this->global->uiControl->link('Media:edit', ['id' => $mediaDTO->id])) /* line 32 */;
			echo '" class="btn btn-light">Edit media</a>
                <a href="';
			echo LR\Filters::escapeHtmlAttr($this->global->uiControl->link('Media:deleteMedia', ['mediaId' => $mediaDTO->id])) /* line 33 */;
			echo '" class="btn btn-light" onclick="return confirm(\'Are you sure you want to delete this media?\')">Delete media</a>
                
                    <label for="status-select-label">Mark as:</label>
                    <select name="status" class="form-select" onchange="updateSelectClass(this)">
';
			foreach ($statusArray as $statusValue => $statusLabel) /* line 37 */ {
				echo '                            <option value="';
				echo LR\Filters::escapeHtmlAttr(json_encode(['mediaId' => $mediaDTO->id, 'status' => $statusValue])) /* line 38 */;
				echo '" ';
				if ($mediaDTO->status->value == $statusValue) /* line 38 */ {
					echo 'selected';
				}
				echo ' class="';
				echo LR\Filters::escapeHtmlAttr($statusLabel) /* line 38 */;
				echo '">
                                ';
				echo LR\Filters::escapeHtmlText($statusLabel) /* line 39 */;
				echo '
                            </option>
';

			}

			echo '                    </select>
                
            </div>
        </div>
    </div>
</div>
';

		}

		echo '
<script>
    document.addEventListener("DOMContentLoaded", function() {
        document.querySelectorAll(\'.form-select\').forEach(function(selectElement) {
            updateSelectClass(selectElement);
        });
    });


document.querySelectorAll(\'.form-select\').forEach(select => {
    select.addEventListener(\'change\', async function () {
    const value = this.value;
    console.log(value);

    const response = await fetch(';
		echo LR\Filters::escapeJs($this->global->uiControl->link('changeStatus!')) /* line 62 */;
		echo ', {
        method: \'POST\',
        headers: {
            \'Content-Type\': \'application/x-www-form-urlencoded\',
            \'X-Requested-With\': \'XMLHttpRequest\'
        },
        body: new URLSearchParams({
            status: value
        })
    });
});
});

function updateSelectClass(selectElement) {
    const states = [\'revisiting\', \'planned\', \'in_progress\', \'completed\', \'on_hold\', \'dropped\'];

    selectElement.classList.remove(...states);

    const selectedOption = selectElement.options[selectElement.selectedIndex];

    const selectedClass = selectedOption.className;

    if (selectedClass) {
        selectElement.classList.add(selectedClass);
    }
}
</script>';
	}
}

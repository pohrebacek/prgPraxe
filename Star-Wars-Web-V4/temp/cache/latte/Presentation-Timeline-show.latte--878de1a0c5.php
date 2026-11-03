<?php

declare(strict_types=1);

use Latte\Runtime as LR;

/** source: /home/rizzek/Documents/GitHub/Star-Wars-Web-V4/Star-Wars-Web-V4/app/Presentation/Timeline/show.latte */
final class Template_878de1a0c5 extends Latte\Runtime\Template
{
	public const Source = '/home/rizzek/Documents/GitHub/Star-Wars-Web-V4/Star-Wars-Web-V4/app/Presentation/Timeline/show.latte';

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
			foreach (array_intersect_key(['mediaDTO' => '14', 'statusValue' => '36', 'statusLabel' => '36'], $this->params) as $ʟ_v => $ʟ_l) {
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
            <div class="line"></div>
            <p>';
			echo LR\Filters::escapeHtmlText($mediaDTO->description) /* line 28 */;
			echo '</p>
            <div class="line2"></div>
            <div class="stav">
                <a href="';
			echo LR\Filters::escapeHtmlAttr($this->global->uiControl->link('Media:edit', ['id' => $mediaDTO->id])) /* line 31 */;
			echo '" class="btn btn-light">Edit media</a>
                <a href="';
			echo LR\Filters::escapeHtmlAttr($this->global->uiControl->link('Media:deleteMedia', ['mediaId' => $mediaDTO->id])) /* line 32 */;
			echo '" class="btn btn-light">Delete media</a>
                
                    <label for="status-select-label">Mark as:</label>
                    <select name="status" class="form-select">
';
			foreach ($statusArray as $statusValue => $statusLabel) /* line 36 */ {
				echo '                            <option value="';
				echo LR\Filters::escapeHtmlAttr(json_encode(['mediaId' => $mediaDTO->id, 'status' => $statusValue])) /* line 37 */;
				echo '" ';
				if ($mediaDTO->status->value == $statusValue) /* line 37 */ {
					echo 'selected';
				}
				echo '>
                                ';
				echo LR\Filters::escapeHtmlText($statusLabel) /* line 38 */;
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
document.querySelectorAll(\'.form-select\').forEach(select => {
    select.addEventListener(\'change\', async function () {
    const value = this.value;
    console.log(value);

    const response = await fetch(';
		echo LR\Filters::escapeJs($this->global->uiControl->link('changeStatus!')) /* line 54 */;
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
</script>';
	}
}

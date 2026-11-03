<?php

declare(strict_types=1);

use Latte\Runtime as LR;

/** source: C:\Users\Honza\PhpstormProjects\Star-Wars-Web-V4\Star-Wars-Web-V4\app\Presentation\Media/edit.latte */
final class Template_0fc22d0491 extends Latte\Runtime\Template
{
	public const Source = 'C:\\Users\\Honza\\PhpstormProjects\\Star-Wars-Web-V4\\Star-Wars-Web-V4\\app\\Presentation\\Media/edit.latte';

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


	/** {block content} on line 1 */
	public function blockContent(array $ʟ_args): void
	{
		extract($this->params);
		extract($ʟ_args);
		unset($ʟ_args);

		$ʟ_tmp = $this->global->uiControl->getComponent('addForm');
		if ($ʟ_tmp instanceof Nette\Application\UI\Renderable) $ʟ_tmp->redrawControl(null, false);
		$ʟ_tmp->render() /* line 2 */;
	}
}

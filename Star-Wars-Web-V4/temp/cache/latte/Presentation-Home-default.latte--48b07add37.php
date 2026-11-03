<?php

declare(strict_types=1);

use Latte\Runtime as LR;

/** source: C:\Users\Honza\PhpstormProjects\Star-Wars-Web-V4\Star-Wars-Web-V4\app\Presentation\Home/default.latte */
final class Template_48b07add37 extends Latte\Runtime\Template
{
	public const Source = 'C:\\Users\\Honza\\PhpstormProjects\\Star-Wars-Web-V4\\Star-Wars-Web-V4\\app\\Presentation\\Home/default.latte';

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

		$this->renderBlock('content', get_defined_vars()) /* line 3 */;
	}


	/** {block content} on line 3 */
	public function blockContent(array $ʟ_args): void
	{
		echo "\n";
	}
}

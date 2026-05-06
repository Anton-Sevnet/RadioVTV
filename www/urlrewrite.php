<?php

$arUrlRewrite = [
	[
		'CONDITION' => '#^/dvtv/?(\\?.*)?$#',
		'RULE' => '',
		'ID' => 'presentation-dyhanie-vtv',
		'PATH' => '/local/presentations/power_system_zapolyarye/index.php',
		'SORT' => 100,
	],
	[
		'CONDITION' => '#^/RadioVTV/?(\\?.*)?$#',
		'RULE' => '',
		'ID' => 'presentation-radiovtv',
		'PATH' => '/local/presentations/power_system_zapolyarye/index.php',
		'SORT' => 100,
	],
	[
		'CONDITION' => '#^/myroomy-uskorenie-bitriks24-dlya-rf/?(\\?.*)?$#',
		'RULE' => '',
		'ID' => 'presentation-myroomy-bitrix24-rf',
		'PATH' => '/local/presentations/myroomy_presentation/index.php',
		'SORT' => 100,
	],
	[
		'CONDITION' => '#^/logo_ex/?(\\?.*)?$#',
		'RULE' => '',
		'ID' => 'presentation-logo-ex',
		'PATH' => '/local/presentations/logo_ex/index.php',
		'SORT' => 100,
	],
	[
		'CONDITION' => '#^/nevskiy-filtr-bitrix24/?(\\?.*)?$#',
		'RULE' => '',
		'ID' => 'presentation-nevskiy-filtr',
		'PATH' => '/local/presentations/nevsky_filter/index.php',
		'SORT' => 100,
	],
];

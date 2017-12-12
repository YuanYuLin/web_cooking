<?php
$info	= new Info(Type::PAGE, 'Dashboard');
$info->set_item('main.ts.php');
$info->set_item('view.html.php');
$info->set_item('view.scss.php');

$info->set_dep('widget_cardgpio');
$info->set_dep('service_gpio');

return $info;
?>

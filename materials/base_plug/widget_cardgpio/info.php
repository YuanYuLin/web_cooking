<?php
$info = new Info(Type::WIDGET, 'Cardgpio');
$info->set_item('main.ts.php');
$info->set_item('view.html.php');
$info->set_item('view.scss.php');

$info->set_dep('widget_switch');
$info->set_dep('service_gpio');
return $info;
?>

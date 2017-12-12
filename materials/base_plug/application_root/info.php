<?php
$info = new Info(Type::APPLICATION, "App");

$info->set_item('app.component.css.php');
$info->set_item('app.component.html.php');
$info->set_item('app.component.ts.php');
$info->set_item('app.module.ts.php');
$info->set_item('app.router.ts.php');

$info->set_dep('widget_sidebar');
$info->set_dep('widget_titlebar');
$info->set_dep('widget_content');
$info->set_dep('service_menu');

return $info;
?>

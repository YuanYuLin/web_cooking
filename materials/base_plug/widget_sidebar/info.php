<?php
$info = new Info(Type::WIDGET, 'Sidebar');
$info->set_item('main.ts.php');
$info->set_item('view.html.php');
$info->set_item('view.scss.php');

$info->set_dep('service_menu');

return $info;
?>

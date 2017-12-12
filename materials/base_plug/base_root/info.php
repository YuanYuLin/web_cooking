<?php
$info = new Info(Type::BASE, 'Root');

//$info->set_item('package.json.php');

$info->set_dep('source_root');
$info->set_dep('application_root');

return $info;
?>

<?php
//var_dump($info);
$htmlobj = $info->htmlobj;
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title><?=$htmlobj->get_title()?></title>
  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
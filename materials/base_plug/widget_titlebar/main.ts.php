<?php
include "plugin.php";
$plugin = new Plugin($info);
$plugin->import("../service_menu/model", "TitlebarMenuT");

$plugin->main_widget();
?>
{
  @Input() TitlebarMenu: TitlebarMenuT;
  constructor() {
  }
}

<?php
include "plugin.php";
$plugin = new Plugin($info);
$plugin->import("../service_menu/model", "SidebarItemT");
$plugin->import("../service_menu/model", "SidebarMenuT");

$plugin->main_widget();
?>
{
  @Input() SidebarMenu: SidebarMenuT;
  @Output() ClickSidebarItem: EventEmitter<SidebarItemT> = new EventEmitter();
  constructor() {
  }
  onclick(Item: SidebarItemT) {
    this.ClickSidebarItem.emit(Item);
  }
}

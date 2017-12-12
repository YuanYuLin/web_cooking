import { Component } from '@angular/core';
import { SidebarItemT } from './lib/service_menu/model';
import { SidebarMenuT } from './lib/service_menu/model';
import { TitlebarMenuT } from './lib/service_menu/model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  SidebarMenu_C: SidebarMenuT;
  TitlebarMenu_C: TitlebarMenuT;
  constructor() {
    this.SidebarMenu_C = {
      Source: 1,
      ItemList: [
<?php
$index = 0;
foreach($this->list as $item_key=>$item) {
  if(($item->type == Type::PAGE)) {
    printf("{ Id: %d, Name: '', Title: '%s', IsShow: true, Url: '#%s' },\n", $index, $item->name, strtolower($item->name));
    $index += 1;
  }
}
?>
      ]
    };
    this.TitlebarMenu_C = {
      Title: this.SidebarMenu_C.ItemList[0].Title,
    };
  }
  ClickSidebarItem_C(Item: SidebarItemT) {
    console.log(Item);
    this.TitlebarMenu_C.Title = Item.Title;
  }
}

<?php
?>
export class SidebarItemT {
  Id: number;
  Name: string;
  Title: string;
  IsShow: boolean;
  Url: string;
}

export class SidebarMenuT {
  Source: number;
  ItemList: Array<SidebarItemT>;
}

export class TitlebarMenuT {
  Title: string;
}

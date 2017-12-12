<?php
?>
<div class="sidebar animate-left">
<div *ngFor="let item of SidebarMenu.ItemList">
<a href="{{item.Url}}" class="sidebar-item sidebar-item-button" (click)="onclick(item)" >{{item.Title}}</a>
</div>
</div>

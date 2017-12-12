<?php
?>
<div class="w3-card-4" *ngFor="let item of GpioList.Items">
 <header class="w3-container w3-blue">
 <h1>{{item.Type}} - {{item.Direction}} - {{item.Port}}:{{item.Pin}}</h1>
 </header>
 <div class="w3-container">
 <p>{{item.Name}}</p>
 <widget-switch [Value]="item.Value" [Style]="Style_C" (ClickSwitch)="item.Value=!item.Value" (change)="onchange($event, item)"></widget-switch>
 </div>
</div> 


<?php
include "plugin.php";
$plugin = new Plugin($info);
$plugin->import("../service_gpio/model", "GpioItemT");
$plugin->import("../service_gpio/model", "GpioListT");
$plugin->import("../service_gpio/main", "ServiceGpio");
$plugin->provider("ServiceGpio");

$plugin->main_widget();
?>
{
  @Input() GpioList: GpioListT;
  Style_C: Array<string>;

  constructor(private serviceGpio: ServiceGpio) {
    this.Style_C = ['slider'];
  }

  onchange(event: MouseEvent, Item: GpioItemT) {
    console.log(Item);
    this.serviceGpio.config(Item.Port, Item.Pin);
  }
}

<?php
include "plugin.php";
$plugin = new Plugin($info);
$plugin->import("../service_gpio/model", "GpioItemT");
$plugin->import("../service_gpio/model", "GpioListT");
$plugin->main_page();
//var_dump($info);
?>
{
  GpioList_C: GpioListT;
  constructor() {
    this.GpioList_C = {
      Items: [
        { Type: 'gpio', Port: 0, Pin: 7, Value: true, Uri: '', Direction: 'output', Name: 'RY2', Comment: '', UnixTimestamp: '' },
        { Type: 'gpio', Port: 0, Pin: 26, Value: false, Uri: '', Direction: 'output', Name: 'DO_Y1', Comment: '', UnixTimestamp: '' },
        { Type: 'gpio', Port: 0, Pin: 27, Value: true, Uri: '', Direction: 'output', Name: 'LED2', Comment: '', UnixTimestamp: '' }
      ]
    };
  }

}

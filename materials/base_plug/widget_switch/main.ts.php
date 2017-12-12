<?php
include "plugin.php";
$plugin = new Plugin($info);

$plugin->main_widget();
?>
{
  @Input() Value: boolean;
  @Input() Style: Array<string>;
  @Output() ClickSwitch: EventEmitter<boolean> = new EventEmitter();

  constructor() {
    this.Style = ['slider', 'round'];
  }

  onswitchclick(value: boolean) {
    this.Value = !value;
    // console.log("BBB" + this.Value + "," + value);
    this.ClickSwitch.emit(this.Value);
  }
}

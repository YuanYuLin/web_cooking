<?php
include 'plugin.php';
$plugin = new Plugin($info);

$plugin->main_service();
?>
{
  messages: string[] = [];
  constructor() {
  }

  config(port: number, pin: number) {
    console.log("port:" + port + ",pin:" + pin);
  }

}


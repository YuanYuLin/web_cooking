<?php
?>
export class GpioItemT {
  Type: string;
  Port: number;
  Pin: number;
  Value: boolean;
  Uri: string;
  Direction: string;
  Name: string;
  Comment: string;
  UnixTimestamp: string;
}

export class GpioListT {
  Items: Array<GpioItemT>;
}


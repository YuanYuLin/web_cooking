<?php
class Info {
  public $type		= "";
  public $name		= "";
  public $selector	= "";
  public $classname	= "";
  public $item		= array();
  public $dep		= array();
  public $ngver		= "";

  function __construct($type, $name)
  {
    $this->type		= $type;
    $this->name		= $name;
    $this->selector	= strtolower($type.'-'.$name);
    $this->classname	= $type.$name;
    $this->dirname	= strtolower($type.'_'.$name);
    if($this->type == Type::NG_VERSION) {
      $this->ngver = $name;
    }
  }

  function set_item($key)
  {
    $this->item[$key] = '';
  }

  function set_dep($key)
  {
    $this->dep[$key] = '';
  }

  function __destruct()
  {
  }
}
?>

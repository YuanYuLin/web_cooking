<?php
class HtmlObj {
  public $info = NULL;
  public $parent_obj = NULL;

  function __construct($parent_obj, $info)
  {
    $this->info = $info;
    $this->parent_obj = $parent_obj;
  }
  function get_title()
  {
    return $this->parent_obj->prjid;
  }
}

$info = new Info(Type::SOURCE, 'Root');
$info->set_item('index.html.php');
$info->set_item('styles.css.php');

$info->htmlobj = new HtmlObj($this, $info);

return $info;
?>

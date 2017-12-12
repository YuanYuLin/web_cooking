<?php
include 'project.php';

$selected_plugs = array(
  'page_dashboard'=>Type::DEFAULT_PAGE,
  'page_firmware'=>'',
  'base_root'=>''
);

if(3 == sizeof($argv)) {
  $src_base = $argv[1];
  $src_plug = $argv[2];

  $ops = new Ops();
  $ops->verify_ngver($src_base);
  $ops->set_prjid(Type::PROJECT_ID_TEST);
  //$ops->set_ngver(Type::NG_VERSION_42);
  $ops->plug_comps($src_plug, $selected_plugs);
  $ops->out_result($src_base);
} else {
  printf("prj <dst_base> <src_plug>\n");
  printf("\tex:  *_prj base_ng42 base_plugin\n");
}

?>

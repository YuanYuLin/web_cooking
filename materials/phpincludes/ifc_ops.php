<?php
class Ops {
  public $list = array();
  public $dep = array();
  public $prjid = 'undefined';
  public $ngver = Type::NG_VERSION_42;

  private function render($filename, $info)
  {
    if (is_file($filename)) {
      $info->ngver = $this->ngver;
      $info->prjid = $this->prjid;
      ob_start();
      include $filename;
      return ob_get_clean();
    }
    return false;
  }

  private function is_info_exist($info)
  {
    if($this->list[$info->classname])
      return true;
    return false;
  }

  private function run_pluginfo($prj_path, $info)
  {
    $info->work_path = '/lib/'.$page;
    if(!$this->is_info_exist($info)){
      printf("Not Exist %d, %s\n", __LINE__, $info->classname);
      $this->list[$info->classname] = $info;
    }
    foreach($info->item as $item_key=>$item_value) {
      $full_path = $prj_path.'/'.$item_key;
      if(is_dir($full_path)) {
        //printf("plug isdir = %s, %s, %s\n", $full_path, $item_key, $item_value);
        $tmp_info = include($full_path.'/info.php');
        if(!$this->is_info_exist($tmp_info)){
          printf("Not Exist %d: %s\n", __LINE__, $tmp_info->classname);
          $this->list[$tmp_info->classname] = $tmp_info;
	  $info = $tmp_info;
	}
        $this->run_pluginfo($prj_path, $info);
      } else {
	//printf("plug isphp = %s, %s, %s\n", $full_path, $item_key, $item_value);
	$info->item_path[$item_key] = $full_path;
	//$info->item_page[$item_key] = $this->render($full_path, $info);
      }
    }
    foreach($info->dep as $dep_key=>$dep_value) {
      //printf("%s, %s\n", $prj_path, $dep_key);
      $full_path = $prj_path.'/../'.$dep_key;
      if(is_dir($full_path)) {
        //printf("dep isdir = %s, %s, %s\n", $full_path, $dep_key, $dep_value);
        $tmp_info = include($full_path.'/info.php');
        if(!$this->is_info_exist($tmp_info)) {
          printf("Not Exist %d, : %s\n", __LINE__, $tmp_info->classname);
          $this->list[$tmp_info->classname] = $tmp_info;
	  $info = $tmp_info;
	}
        $this->run_pluginfo($full_path, $info);
      } else {
	//printf("dep isfile = %s, %s, %s\n", $full_path, $dep_key, $dep_value);
      }
    }
  }

  public function plug_comps($src_plug, $supported_pages)
  {
    foreach($this->list as $item_key=>$item_value) {
      if((Type::BASE == $item_value->type) && ("Root" == $item_value->name)) {
        printf("%s, %s\n", $item_key, $item_value->work_path);
      }
    }
    //var_dump($supported_pages);
    foreach($supported_pages as $pkg=>$value) {
      $pkg_path = $src_plug.'/'.$pkg;
      $info = include($pkg_path.'/info.php');
      $info->is_defaultpage = false;
      if($value == Type::DEFAULT_PAGE) {
        $info->is_defaultpage = true;
      }
      $this->run_pluginfo($pkg_path, $info);
    }
  }

  public function out_result($output_dir)
  {
    foreach($this->list as $obj_key=>$obj) {
      printf(">>>>>%s:%d files\n", $obj_key, sizeof($obj->item));
      //var_dump($obj);
      foreach($obj->item as $item_key =>$page) {
        $file_part=pathinfo($obj->item_path[$item_key]);
	$file_dirname = realpath($file_part['dirname']);
	$file_extension = $file_part['extension'];
	$file_filename = $file_part['filename'];
	$file_basename = $file_part['basename'];

	$input_php = $file_dirname.'/'.$file_basename;
	$output_root = $output_dir.Type::PATH[$obj->type];

	if(($obj->type == Type::PAGE)||($obj->type == Type::WIDGET)||($obj->type == Type::SERVICE)) {
          $output_root = $output_root.strtolower($obj->type.'_'.$obj->name);
	}
	if(!file_exists($output_root)) {
          mkdir($output_root, 0777, true);
	}
	$output_file = $output_root.'/'.$file_filename;

	//printf("%s-%s\n", $item_key, $obj->type);
	//printf("src:%s\n", $input_php);
	//printf("dst:%s\n", $output_file);
	file_put_contents($output_file, $this->render($input_php, $obj));
      }
      printf("<<<<<\n");
    }
  }

  public function set_prjid($prjid)
  {
    $this->prjid = $prjid;
  }

  public function set_ngver($ngver)
  {
    $this->ngver = $ngver;
  }

  public function verify_ngver($base_src)
  {
    $tmp_info = include($base_src.'/info.php');
    $this->set_ngver($tmp_info->ngver);
  }
}
?>

<?php
class Plugin {
  //private $import_list = NULL;
  private $info = NULL;
  //private $provider_list = NULL;

public function __construct($info)
{
  $this->info = $info;
  $this->info->import_list = array();
  $this->info->provider_list = array();
}

public function main_widget()
{
  $type = $this->info->type;
  if($type == Type::WIDGET) {
    $this->import('@angular/core', 'Component');
    $this->import('@angular/core', 'Input');
    $this->import('@angular/core', 'Output');
    $this->import('@angular/core', 'EventEmitter');

    foreach($this->info->import_list as $key=>$val) {
      printf("import { %s } from '%s';\n", $key, $val);
    }
    printf("@Component({\n");
    printf("selector: '%s',\n", $this->info->selector);
    $provider_list_len = sizeof($this->info->provider_list);
    $p_index = 0;
    if($provider_list_len > 0) {
      printf("providers:[");
      foreach($this->info->provider_list as $p_key=>$p_val) {
        if($p_index == ($provider_list_len - 1)) {
          printf("%s", $p_key);
	} else {
	  printf("%s,", $p_key);
	}
      }
      printf("],\n");
    }
    printf("templateUrl: './view.html',\n");
    printf("styleUrls: ['./view.scss']\n");
    printf("})\n");
    printf("export class %s\n", $this->info->classname);
  }
}

public function main_page()
{
  $type = $this->info->type;
  if($type == Type::PAGE) {
    $this->import('@angular/core', 'Component');
    $this->import('@angular/core', 'Input');
    $this->import('@angular/core', 'Output');
    $this->import('@angular/core', 'EventEmitter');

    foreach($this->info->import_list as $key=>$val) {
      printf("import { %s } from '%s';\n", $key, $val);
    }
    printf("@Component({\n");
    printf("selector: '%s',\n", $this->info->selector);
    $provider_list_len = sizeof($this->info->provider_list);
    $p_index = 0;
    if($provider_list_len > 0) {
      printf("providers:[");
      foreach($this->info->provider_list as $p_key=>$p_val) {
        if($p_index == ($provider_list_len - 1)) {
          printf("%s", $p_key);
	} else {
	  printf("%s,", $p_key);
	}
      }
      printf("],\n");
    }
    printf("templateUrl: './view.html',\n");
    printf("styleUrls: ['./view.scss']\n");
    printf("})\n");
    printf("export class %s\n", $this->info->classname);
  }
}

/*
 * import
 */
public function import($path, $class)
{
  $this->info->import_list[$class] = $path;
}

/*
 * provider
 */
public function provider($class)
{
  $this->info->provider_list[$class] = '';
}

/*
 *
 */
public function main_service()
{
  $type = $this->info->type;
  $ngversion = $this->info->ngver;
  if(($type == Type::SERVICE)) {
    //var_dump($this);
    $this->import('@angular/core', 'Injectable');
    switch($ngversion) {
      case Type::NG_VERSION_42:
        $this->import('@angular/http', 'HttpModule');
      break;
      case Type::NG_VERSION_43:
        $this->import('@angular/common/http', 'HttpClientModule');
      break;
    }
    foreach($this->info->import_list as $key=>$val) {
      printf("import { %s } from '%s';\n", $key, $val);
    }
    printf("@Injectable()\n");
    printf("export class %s\n", $this->info->classname);
  }
}
  
}// End Class
?>

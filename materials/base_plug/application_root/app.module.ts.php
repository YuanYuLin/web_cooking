<?php
//var_dump($this->list);
?>
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Routing } from './app.router';

import { AppComponent }	from './app.component';
<?php
$import_http_module = false;
$include_modules = array();
$ngversion = $this->ngver;
foreach($this->list as $item_key=>$item) {
  //printf("%s\n", $item_key);
  if(($item->type == Type::PAGE) || ($item->type == Type::WIDGET)) {
    $classname = $item->classname;
    $dirname = strtolower('./lib/'.$item->type.'_'.$item->name.'/main');
    //printf("import { %s } from './lib/%s/main';\n", $classname, $dirname);
    $include_modules[$item->classname] = $dirname;
  }
  if(($item->type == Type::SERVICE)) {
    $import_http_module = true;
    //$include_modules['HttpModule'] = '@angular/http';
  }
}
foreach($include_modules as $key=>$val) {
  printf("import { %s } from '%s';\n", $key, $val);
}
if($import_http_module) {
  switch($ngversion) {
    case Type::NG_VERSION_42:
      printf("import { HttpModule } from '@angular/http';\n");
    break;
    case Type::NG_VERSION_43:
      printf("import { HttpClientModule } from '@angular/common/http';\n");
    break;
  }
}
?>

@NgModule({
  declarations: [
<?php
foreach($include_modules as $key=>$val) {
    printf("%s,\n", $key);
}
?>
    AppComponent
  ],
  imports: [
<?php
if($import_http_module) {
  switch($ngversion) {
    case Type::NG_VERSION_42:
      printf("%s,\n", "HttpModule");
    break;
    case Type::NG_VERSION_43:
      printf("%s,\n", "HttpClientModule");
    break;
  }
}
?>
    Routing,
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

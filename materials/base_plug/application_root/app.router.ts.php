<?php
?>

import { ModuleWithProviders } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

/** App Components **/
<?php
foreach($this->list as $item_key=>$item) {
  if(($item->type == Type::PAGE)) {
    $classname = $item->classname;
    $dirname = strtolower($item->type.'_'.$item->name);
?>
import { <?=$classname?> } from './lib/<?=$dirname?>/main';
<?php
  }
}
?>

export const routes: Routes = [
<?php
$defaultpage_name = '';
foreach($this->list as $item_key=>$item) {
  if(($item->type == Type::PAGE)) {
    $classname = $item->classname;
    $dirname = strtolower($item->name);
    if($item->is_defaultpage) {
      $defaultpage_name = $dirname;
    }
?>
  {
    path: '<?=$dirname?>',
    component: <?=$classname?>

  },
<?php
  }
}
?>
  {
    path: '',
    redirectTo: '<?=$defaultpage_name?>',
    pathMatch: 'full'
  },
  {
    path: '**',
    redirectTo: '<?=$defaultpage_name?>'
  }
];

export const Routing: ModuleWithProviders = RouterModule.forRoot(routes, { useHash: true });

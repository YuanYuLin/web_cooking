<?php
/*
 * Folder layout
 * Base				/ 
 *   +-Source			/src
 *       +-Application		/src/app
 *           +-Library
 *               +-Page		/src/app/lib
 *               +-Widget	/src/app/lib
 *               +-Service	/src/app/lib
 */
class Type {
  const BASE		= "Base";
  const SOURCE		= "Source";
  const APPLICATION	= "Application";
  const PAGE		= "Page";
  const WIDGET		= "Widget";
  const SERVICE		= "Service";
  const PATH = array(
    Type::BASE		=> '/',
    Type::SOURCE	=> '/src/',
    Type::APPLICATION	=> '/src/app/',
    Type::PAGE		=> '/src/app/lib/',
    Type::WIDGET	=> '/src/app/lib/',
    Type::SERVICE	=> '/src/app/lib/',
  );

  const DEFAULT_PAGE	= 'default_page';

  const NG_VERSION	= 'NGVersion';
  const NG_VERSION_42	= 'ng42';
  const NG_VERSION_50	= 'ng50';

  const PROJECT_ID_TEST	= 'prjid::test';
}
?>

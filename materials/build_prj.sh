#!/bin/bash

PRJ_NAME=$1
PRJ_FOUND="no"
SYM_NAME_BASE_NG="base_ng"
if [ "$PRJ_NAME" == "Test" ]; then
  PRJ_FOUND="yes"
  NAME_PRJ="project/prj_test.php"
  NAME_BASE_NG="base_ng42"
fi

if [ "$PRJ_FOUND" == "yes" ]; then
  echo "php $NAME_PRJ $NAME_BASE_NG base_plug"
  rm -f $SYM_NAME_BASE_NG
  ln -s $NAME_BASE_NG $SYM_NAME_BASE_NG
  $PHPROOT/bin/php $NAME_PRJ $SYM_NAME_BASE_NG base_plug/
  cd $SYM_NAME_BASE_NG
  $NODEJSROOT/bin/ng build -prod
fi

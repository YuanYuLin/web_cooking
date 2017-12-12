#!/bin/bash

PRJ_NAME=$1
NG_STATUS_FILE="$NODEJSROOT/ng_installed"

if [ -f $NG_STATUS_FILE ]; then
  echo "angular cli already installed"
  $NODEJSROOT/bin/ng -v
else
  echo "$NODEJSROOT/bin/npm install -g @angular/cli"
  echo "$PATH"
  export PATH=$PATH:$NODEJSROOT/bin
  echo "$PATH"

  #node -v
  npm install -g @angular/cli
  if [ -f $NODEJSROOT/bin/ng ]; then
    touch $NG_STATUS_FILE
  fi
fi

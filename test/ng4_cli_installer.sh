#!/bin/bash

PRJ_NAME=$1

echo "$NODEJSROOT/bin/npm install -g @angular/cli"
echo "$PATH"
export PATH=$PATH:$NODEJSROOT/bin
echo "$PATH"

#node -v
npm install -g @angular/cli

#echo "$NODEJSROOT/bin/ng new $PRJ_NAME"
#ng new $PRJ_NAME


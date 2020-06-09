#! /bin/bash

if [ -z $1 ]; then
    echo "lib name required"
    exit 1
fi

IS_INSTALLED=`pip list | grep "$1"`

if [ -z "$IS_INSTALLED" ]; then
    echo 0
else
    echo 1
fi

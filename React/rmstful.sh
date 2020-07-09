#!/bin/bash

if [ -d "../src/components/$1" ]; then
  echo "$1 component already exists"
  echo "removing $1 component"
  rm -r "../src/components/$1"
  echo "removed"
  exit 1
else
  echo "component doesn't exists"
fi

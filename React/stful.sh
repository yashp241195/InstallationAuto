#!/bin/bash

componentName=$1
if [ "$2" == "withcss" ]; then withCSS=true; else withCSS=false; fi

if [ -d "../src/components/$componentName" ]; then
  echo " $1 component already exists"
  exit 1
fi

mkdir ../src/components/$componentName
touch ../src/components/$componentName/$componentName.js

importcss=""

if [ "$withCSS" == true ]; then
  touch ../src/components/$componentName/$componentName.css
  importcss="import './$componentName.css';"
fi

echo "component folder created .."


cat << EOF >> ../src/components/$componentName/$componentName.js
import React, {Component} from 'react';
$importcss

class $componentName extends Component{
  
  /*
    $componentName is defined as a stateful component
  */

  render(){
    
    return(
        <div>$componentName</div>
    );

  }


}

export default $componentName;
EOF

echo "components created"

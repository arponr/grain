#!/bin/bash

dir="$HOME/Documents/grain"

python "$dir/grain.py" ${@:1}
source "$dir/bashout.sh"
rm "$dir/bashout.sh"

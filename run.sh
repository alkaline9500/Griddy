#!/bin/bash
mkdir -p gen/
find $1 -print | grep 'mp4$\|avi$\|mkv$' | python posterize.py > index.html

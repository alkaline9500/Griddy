#!/bin/bash
find $1 -print | grep 'mp4$\|avi$\|mkv$' | python posterize.py > gen/index.html

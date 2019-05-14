#!/bin/bash

root="/d/project/blog2/source/_posts"
dt=$(date +%Y年%m月%d日%H时%M分%S秒)
dt="backup于$dt"
newd="${root}/_backups/$dt"
mkdir $newd
cp -r ${root}/#* ${newd}/
cp -r ${root}/_ignore ${newd}/
cp -r ${root}/*.md ${newd}/

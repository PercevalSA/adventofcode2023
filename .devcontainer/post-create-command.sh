#!/bin/bash

# install all requirements to solve all problems
for folder in $(ls -d */);
do 
    python3 -m pip install -r ${folder}requirements.txt;
done
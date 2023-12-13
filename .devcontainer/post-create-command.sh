#!/bin/bash

# install all requirements to solve all problems
for folder in $(ls -d */);
do
    requirements="${folder}requirements.txt"
    if [ -f "${requirements}" ];
    then
        python3 -m pip install -r ${requirements};
    fi
done
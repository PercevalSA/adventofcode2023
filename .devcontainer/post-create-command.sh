#!/bin/bash

# install all requirements: global and for each project
for folder in $(ls -d *) $(ls -d);
do
    requirements="${folder}/requirements.txt"
    if [ -f "${requirements}" ];
    then
        python3 -m pip install -r ${requirements};
    fi
done

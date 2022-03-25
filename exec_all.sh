#!/bin/bash
for i in {0..14}
do
    cd ./ex$(printf "%02d" $i)/
    ./ex$(printf "%02d" $i).py
    cd ..
done
ls -la
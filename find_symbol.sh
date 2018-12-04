#!/bin/bash

for file in `find ./ -type f ! -name "*.*"`;
do 
	grep $@ $file
done
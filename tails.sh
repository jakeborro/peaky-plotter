#!/bin/bash
mkdir -p ~/Peaks/Data/"$(date -I)"

for file in ~/Peaks/Data/*.history;
    do tail -n 32 $file > $file.csv
done

for file in ~/Peaks/Data/*.history.csv;
    do mv $file  ~/Peaks/Data/"$(date -I)"
done

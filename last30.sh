#!/usr/bin/env bash
find . -type f \( -name "*.history.csv" \) -exec tail -n 32 "$file" {} + > "$file"extract.csv

awk '!/==>/' extract.csv > temp && mv temp extracted.csv

awk -F "," '{print $0 >> ("file" $1 ".history.csv")}' extracted.csv

import csv
import os
import glob

path = '/path/to/file'
for infile in glob.glob( os.path.join(path, '*.history.csv') ):
    output = infile + '.out'
    with open(infile, 'r') as source:
        readr = csv.reader(source)
        with open(output,"w") as result:
            writr = csv.writer(result)
            for r in readr:
                writr.writerow((r[4], r[2]))

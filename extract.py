import csv
import glob

def main():
    files = glob.glob('./*.history')

    for file in files:
        with open(file,"rb") as source:
            readr = csv.reader(source)
            with open(file + '.csv' ,"wb") as result:
                writr = csv.writer(result)
                for r in readr:
                    writr.writerow((r[4], r[2]))
main()

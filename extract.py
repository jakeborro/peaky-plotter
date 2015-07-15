import csv

with open("data.csv","rb") as source:
    readr = csv.reader(source)
    with open("data2.csv","wb") as result:
        writr = csv.writer(result)
        for r in readr:
            writr.writerow((r[2], r[4]))

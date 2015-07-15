import csv

remove_from = 2
remove_to = 5

with open("data.csv", "rb") as fp_in, open("data2.csv", "wb") as fp_out:
    reader = csv.reader(fp_in, delimiter=",")
    writer = csv.writer(fp_out, delimiter=",")
    for row in reader:
        del row[remove_from:remove_to]
        writer.writerow(row)

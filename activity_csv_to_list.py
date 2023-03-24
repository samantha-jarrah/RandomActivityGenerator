import csv

activities = []

with open("Activity_List.csv", "r") as infile:
    csvreader = csv.reader(infile)
    next(csvreader)

    for row in csvreader:
        activities.append(row)

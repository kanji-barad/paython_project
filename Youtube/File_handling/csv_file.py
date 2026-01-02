import csv

with open("/Users/kanjibarad/Documents/Python+main_batch/Youtube/File_handling/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

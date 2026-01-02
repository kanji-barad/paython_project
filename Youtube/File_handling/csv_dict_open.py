import csv

with open("/Users/kanjibarad/Documents/Python+main_batch/Youtube/File_handling/data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"], row["city"])

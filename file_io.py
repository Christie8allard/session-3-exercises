import csv

with open('dogs_are_awesome.csv') as file: #file is the variale name and can be anything
    reader = csv.reader(file)
    for row in reader:
        print(row)

#reader for reading
#writing for writing csv


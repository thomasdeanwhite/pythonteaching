import csv
import re

def read_csv(filename, headers=True):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = {}
        heads = []
        for row in csv_reader:
            if headers:
                headers = False
                for c in row:
                    heads.append(c)
                    data[c] = []
            else:
                for i in range(len(row)):
                    if not re.match("^\d+?\.\d+?$", row[i]) is None:
                        row[i] = float(row[i])
                    data[heads[i]].append(row[i])
        return data
    return {}

data = read_csv("data/training.csv")

print(data)
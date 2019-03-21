import csv
import re

def read_csv(filename, headers=True, heads=[]):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = {}

        for row in csv_reader:
            # construct a table of headers
            if headers:
                headers = False
                for c in row:
                    heads.append(c)
                    data[c] = []
            else:
                for i in range(len(row)):
                    # is input a floating point number?
                    if not re.match("^\d+?\.\d+?$", row[i]) is None:
                        # convert to float
                        row[i] = float(row[i])
                    data[heads[i]].append(row[i])
        return data
    return {}

data = read_csv("data/training.csv")

print(data)
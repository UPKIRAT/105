import statistics
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
array = []
# array.append(data)

for i in data:
    a = int(i)
    array.append(a)

final = statistics.stdev(array)
print(final)
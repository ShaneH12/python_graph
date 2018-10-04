import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
County = []
Population = []

with open("louisiana_cen2.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        County.append(row[0])
        Population.append(int(row[1]))

plt.bar(County, Population)
plt.xticks(rotation=90)
plt.show()

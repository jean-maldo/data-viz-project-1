import csv
from collections import defaultdict

def default_factory():
    return [0, None, None, 0]

reader = csv.DictReader(open('../data/tests/aggregate_airlines.csv', newline=''))
airlines = defaultdict(default_factory)
for row in reader:
    number_of_delays = 0
    if(row["ARR_DELAY"].isdigit()):
        delayed_hours = int(row["ARR_DELAY"])
    else:
        delayed_hours = 0
    
    print(delayed_hours)
    airlines[row["UNIQUE_CARRIER"]][0] += delayed_hours
    max = airlines[row["UNIQUE_CARRIER"]][1]
    airlines[row["UNIQUE_CARRIER"]][1] = delayed_hours if max is None else delayed_hours if delayed_hours > max else max
    min = airlines[row["UNIQUE_CARRIER"]][2]
    airlines[row["UNIQUE_CARRIER"]][2] = delayed_hours if min is None else delayed_hours if delayed_hours < min else min
    airlines[row["UNIQUE_CARRIER"]][3] += 1
for airline in airlines:
    airlines[airline][3] = airlines[airline][0]/airlines[airline][3] # calculate mean

writer = csv.writer(open('out.csv', 'w', newline = ''))
writer.writerow(["UNIQUE_CARRIER", "ARR_DELAY", "max", "min", "mean"])
writer.writerows([airline] + airlines[airline] for airline in airlines)
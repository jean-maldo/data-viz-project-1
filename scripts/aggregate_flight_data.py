import csv, sys
from collections import defaultdict

def default_factory():
    return [0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reader = csv.DictReader(open('../data/tests/aggregate_airlines.csv', newline=''))
airlines = defaultdict(default_factory)
for row in reader:
    if(row["ARR_DELAY"].isdigit()):
        delayed_hours = int(row["ARR_DELAY"]) # negative values are parsed as 0
    else:
        delayed_hours = 0
        
    if (delayed_hours):
        airlines[row["UNIQUE_CARRIER"]][1] += 1
    
    airlines[row["UNIQUE_CARRIER"]][0] += delayed_hours
    min = airlines[row["UNIQUE_CARRIER"]][2] if airlines[row["UNIQUE_CARRIER"]][2] != 0 else sys.maxsize
    airlines[row["UNIQUE_CARRIER"]][2] = delayed_hours if min is None else delayed_hours if delayed_hours < min and delayed_hours > 0 else min
    max = airlines[row["UNIQUE_CARRIER"]][3]
    airlines[row["UNIQUE_CARRIER"]][3] = delayed_hours if max is None else delayed_hours if delayed_hours > max else max
    
    if(row["ARR_DELAY_GROUP"].isdigit()):
        if int(row["ARR_DELAY_GROUP"]) == 1:
            airlines[row["UNIQUE_CARRIER"]][5] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 2:
            airlines[row["UNIQUE_CARRIER"]][6] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 3:
            airlines[row["UNIQUE_CARRIER"]][7] += 1
        elif  int(row["ARR_DELAY_GROUP"]) == 4:
            airlines[row["UNIQUE_CARRIER"]][8] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 5:
            airlines[row["UNIQUE_CARRIER"]][9] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 6:
            airlines[row["UNIQUE_CARRIER"]][10] += 1
        elif  int(row["ARR_DELAY_GROUP"]) == 7:
            airlines[row["UNIQUE_CARRIER"]][11] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 8:
            airlines[row["UNIQUE_CARRIER"]][12] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 9:
            airlines[row["UNIQUE_CARRIER"]][13] += 1
        
for airline in airlines:
    airlines[airline][4] = airlines[airline][0]/airlines[airline][1] # calculate mean

writer = csv.writer(open('../data/processed/delays_cancellations_by_airline.csv', 'w', newline = ''))
writer.writerow(["AIRLINE", "DELAY_MINS_TOTAL", "NUM_DELAYS", "MIN_DELAY", "MAX_DELAY", "MEAN", "GRP_1_TOTAL", "GRP_2_TOTAL", "GRP_3_TOTAL", "GRP_4_TOTAL", "GRP_5_TOTAL", "GRP_6_TOTAL", "GRP_7_TOTAL", "GRP_8_TOTAL", "GRP_9_TOTAL"])
writer.writerows([airline] + airlines[airline] for airline in airlines)
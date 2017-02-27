import csv, sys
from collections import defaultdict

def default_factory():
    return [0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#file = '../data/tests/aggregate_airlines.csv'7
file = '../data/flights_delayed_cancelled/flights_delayed_cancelled.csv'

reader = csv.DictReader(open(file, newline=''))
airlines = defaultdict(default_factory)
for row in reader:
    month = row["MONTH"]
    month = int(month)
    
    if(row["ARR_DELAY"].isdigit()):
        delayed_hours = int(row["ARR_DELAY"]) # negative values are parsed as 0
    else:
        delayed_hours = 0
        
    if (delayed_hours):
        airlines[row["UNIQUE_CARRIER"], month][1] += 1
    
    airlines[row["UNIQUE_CARRIER"], month][0] += delayed_hours
    min = airlines[row["UNIQUE_CARRIER"], month][2] if airlines[row["UNIQUE_CARRIER"], month][2] != 0 else sys.maxsize
    airlines[row["UNIQUE_CARRIER"], month][2] = delayed_hours if min is None else delayed_hours if delayed_hours < min and delayed_hours > 0 else min
    max = airlines[row["UNIQUE_CARRIER"], month][3]
    airlines[row["UNIQUE_CARRIER"], month][3] = delayed_hours if max is None else delayed_hours if delayed_hours > max else max
    
    if(row["ARR_DELAY_GROUP"].isdigit()):
        if int(row["ARR_DELAY_GROUP"]) == 1:
            airlines[row["UNIQUE_CARRIER"], month][4] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 2:
            airlines[row["UNIQUE_CARRIER"], month][5] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 3:
            airlines[row["UNIQUE_CARRIER"], month][6] += 1
        elif  int(row["ARR_DELAY_GROUP"]) == 4:
            airlines[row["UNIQUE_CARRIER"], month][7] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 5:
            airlines[row["UNIQUE_CARRIER"], month][8] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 6:
            airlines[row["UNIQUE_CARRIER"], month][9] += 1
        elif  int(row["ARR_DELAY_GROUP"]) == 7:
            airlines[row["UNIQUE_CARRIER"], month][10] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 8:
            airlines[row["UNIQUE_CARRIER"], month][11] += 1
        elif int(row["ARR_DELAY_GROUP"]) == 9:
            airlines[row["UNIQUE_CARRIER"], month][12] += 1
    
    if(row["DAY_OF_WEEK"].isdigit()):
        if int(row["DAY_OF_WEEK"]) == 1:
            airlines[row["UNIQUE_CARRIER"], month][13] += 1
            airlines[row["UNIQUE_CARRIER"], month][14] += delayed_hours
        elif int(row["DAY_OF_WEEK"]) == 2:
            airlines[row["UNIQUE_CARRIER"], month][15] += 1
            airlines[row["UNIQUE_CARRIER"], month][16] += delayed_hours
        elif int(row["DAY_OF_WEEK"]) == 3:
            airlines[row["UNIQUE_CARRIER"], month][17] += 1
            airlines[row["UNIQUE_CARRIER"], month][18] += delayed_hours
        elif  int(row["DAY_OF_WEEK"]) == 4:
            airlines[row["UNIQUE_CARRIER"], month][19] += 1
            airlines[row["UNIQUE_CARRIER"], month][20] += delayed_hours
        elif int(row["DAY_OF_WEEK"]) == 5:
            airlines[row["UNIQUE_CARRIER"], month][21] += 1
            airlines[row["UNIQUE_CARRIER"], month][22] += delayed_hours
        elif int(row["DAY_OF_WEEK"]) == 6:
            airlines[row["UNIQUE_CARRIER"], month][23] += 1
            airlines[row["UNIQUE_CARRIER"], month][24] += delayed_hours
        elif  int(row["DAY_OF_WEEK"]) == 7:
            airlines[row["UNIQUE_CARRIER"], month][25] += 1
            airlines[row["UNIQUE_CARRIER"], month][26] += delayed_hours
        
        if(row["CARRIER_DELAY"].isdigit()):
            airlines[row["UNIQUE_CARRIER"], month][27] += int(row["CARRIER_DELAY"])
            airlines[row["UNIQUE_CARRIER"], month][28] += 1
        
        if(row["WEATHER_DELAY"].isdigit()):
            airlines[row["UNIQUE_CARRIER"], month][29] += int(row["WEATHER_DELAY"])
            airlines[row["UNIQUE_CARRIER"], month][30] += 1
        
        if(row["NAS_DELAY"].isdigit()):
            airlines[row["UNIQUE_CARRIER"], month][31] += int(row["NAS_DELAY"])
            airlines[row["UNIQUE_CARRIER"], month][32] += 1
        
        if(row["SECURITY_DELAY"].isdigit()):
            airlines[row["UNIQUE_CARRIER"], month][33] += int(row["SECURITY_DELAY"])
            airlines[row["UNIQUE_CARRIER"], month][34] += 1
        
        if(row["LATE_AIRCRAFT_DELAY"].isdigit()):
            airlines[row["UNIQUE_CARRIER"], month][35] += int(row["LATE_AIRCRAFT_DELAY"])
            airlines[row["UNIQUE_CARRIER"], month][36] += 1
        
        if(int(row["CANCELLED"]) == 1):
            airlines[row["UNIQUE_CARRIER"], month][37] += 1
        
        if(row["CANCELLATION_CODE"] == "A"):
            airlines[row["UNIQUE_CARRIER"], month][38] += 1
        
        if(row["CANCELLATION_CODE"] == "B"):
            airlines[row["UNIQUE_CARRIER"], month][39] +=1
        
        if(row["CANCELLATION_CODE"] == "C"):
            airlines[row["UNIQUE_CARRIER"], month][40] +=1
        
        if(row["CANCELLATION_CODE"] == "D"):
            airlines[row["UNIQUE_CARRIER"], month][41] +=1
        
        if(row["ARR_DEL15"] == "1"):
            airlines[row["UNIQUE_CARRIER"], month][42] += delayed_hours
        
        if(row["ARR_DEL15"] == "1"):
            airlines[row["UNIQUE_CARRIER"], month][43] +=1
        
for airline in airlines:    
    if(airlines[airline[0], airline[1]][2] == sys.maxsize):
        airlines[airline[0], airline[1]][2] = None
    
    if(airlines[airline[0], airline[1]][3] == 0):
        airlines[airline[0], airline[1]][3] = None
        
out_file = '../data/processed/delays_cancellations_by_airline_2016.csv'
writer = csv.writer(open(out_file, 'w', newline = ''))
writer.writerow(["AIRLINE", "MONTH", "DELAY_MINS_TOTAL", "TOTAL_DELAYS", "MIN_DELAY", "MAX_DELAY", "GRP_1_TOTAL", "GRP_2_TOTAL", "GRP_3_TOTAL", "GRP_4_TOTAL", "GRP_5_TOTAL", "GRP_6_TOTAL", "GRP_7_TOTAL", "GRP_8_TOTAL", "GRP_9_TOTAL", "MON_TOTAL_DELAYS", "MON_HOURS_DELAY", "TUE_TOTAL_DELAYS", "TUE_HOURS_DELAY", "WED_TOTAL_DELAYS", "WED_HOURS_DELAY", "THU_TOTAL_DELAYS", "THU_HOURS_DELAY", "FRI_TOTAL_DELAYS", "FRI_HOURS_DELAY", "SAT_TOTAL_DELAYS", "SAT_HOURS_DELAY", "SUN_TOTAL_DELAYS", "SUN_HOURS_DELAY", "CARRIER_DELAY_MINS", "CARRIER_DELAY_TOTAL", "WEATHER_DELAY_MINS", "WEATHER_DELAY_TOTAL", "NAS_DELAY_MINS", "NAS_DELAY_TOTAL", "SECURITY_DELAY_MINS", "SECURITY_DELAY_TOTAL", "LATE_AIRCRAFT_DELAY_MINS", "LATE_AIRCRAFT_DELAY_TOTAL", "CANCELLED_TOTAL", "CANCELLATIONS_CARRIER", "CANCELLATIONS_WEATHER", "CANCELLATIONS_NAS", "CANCELLATIONS_SECURITY", "DEL15_MINS", "DEL15_TOTAL"])
writer.writerows([airline[0]] + [airline[1]] + airlines[airline] for airline in airlines)
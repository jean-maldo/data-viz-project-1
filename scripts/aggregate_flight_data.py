import csv, sys
from collections import defaultdict

def default_factory():
    return [0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # intialize values

#file = '../data/tests/aggregate_airlines.csv'7
#file = '../data/flights_delayed_cancelled/01jan.csv'
file = '../data/all_flights/flights.csv' # file to read from
out_file = '../data/processed/flights_by_airline_2016.csv' # file to write to

reader = csv.DictReader(open(file, newline=''))
airlines = defaultdict(default_factory)
for row in reader:
    # variables for fields read in
    month = row["MONTH"]
    arrival_delay = row["ARR_DELAY"]
    unique_carrier = row["UNIQUE_CARRIER"]
    arrival_delay_group = row["ARR_DELAY_GROUP"]
    day_of_week = row["DAY_OF_WEEK"]
    carrier_delay = row["CARRIER_DELAY"]
    weather_delay = row["WEATHER_DELAY"]
    nas_delay = row["NAS_DELAY"]
    security_delay = row["SECURITY_DELAY"]
    late_aircraft_delay = row["LATE_AIRCRAFT_DELAY"]
    cancelled = row["CANCELLED"]
    cancellation_code = row["CANCELLATION_CODE"]
    
    if(arrival_delay.isdigit()): # filters negative values
        delayed_hours = int(arrival_delay)
        delayed_hours = 0 if delayed_hours < 15 else delayed_hours
    else:
        delayed_hours = 0
        
    if (delayed_hours): # check for values
        airlines[unique_carrier, month][1] += 1 # count delays
    
    airlines[unique_carrier, month][0] += delayed_hours # sum delayed hours
    #calculate min
    min = airlines[unique_carrier, month][2] if airlines[unique_carrier, month][2] != 0 else sys.maxsize
    airlines[unique_carrier, month][2] = delayed_hours if min is None else delayed_hours if delayed_hours < min and delayed_hours > 0 else min
    # calculate max
    max = airlines[unique_carrier, month][3]
    airlines[unique_carrier, month][3] = delayed_hours if max is None else delayed_hours if delayed_hours > max else max
    
    if(delayed_hours >= 15):
        if arrival_delay_group == "1":
            airlines[unique_carrier, month][4] += 1 # count delays of length 15-29 mins
        elif arrival_delay_group == "2":
            airlines[unique_carrier, month][5] += 1 # count delays of length 30-44 mins
        elif arrival_delay_group == "3":
            airlines[unique_carrier, month][6] += 1 # count delays of length 45-59 mins
        elif  arrival_delay_group == "4":
            airlines[unique_carrier, month][7] += 1 # count delays of length 60-74 mins
        elif arrival_delay_group == "5":
            airlines[unique_carrier, month][8] += 1 # count delays of length 75-89 mins
        elif arrival_delay_group == "6":
            airlines[unique_carrier, month][9] += 1 # count delays of length 90-104 mins
        elif  arrival_delay_group == "7":
            airlines[unique_carrier, month][10] += 1 # count delays of length 105-119 mins
        elif arrival_delay_group == "8":
            airlines[unique_carrier, month][11] += 1 # count delays of length 120-134 mins
        elif arrival_delay_group == "9":
            airlines[unique_carrier, month][12] += 1 # count delays of length 135-149 mins
        elif arrival_delay_group == "10":
            airlines[unique_carrier, month][13] += 1 # count delays of length 150-164 mins
        elif arrival_delay_group == "11":
            airlines[unique_carrier, month][14] += 1 # count delays of length 165-179 mins
        elif arrival_delay_group == "12":
            airlines[unique_carrier, month][15] += 1 # count delays of length >= 180 mins        
    
    if(delayed_hours >= 15):
        if day_of_week == "1":
            airlines[unique_carrier, month][16] += 1 # count delays for Monday
            airlines[unique_carrier, month][17] += delayed_hours # count hours for delays on Monday
        elif day_of_week == "2":
            airlines[unique_carrier, month][18] += 1 # count delays for Tuesday
            airlines[unique_carrier, month][19] += delayed_hours # count hours for delays on Tuesday
        elif day_of_week == "3":
            airlines[unique_carrier, month][20] += 1 # count delays for Wednesday
            airlines[unique_carrier, month][21] += delayed_hours # count hours for delays on Wednesday
        elif  day_of_week == "4":
            airlines[unique_carrier, month][22] += 1 # count delays for Thursday
            airlines[unique_carrier, month][23] += delayed_hours # count hours for delays on Thursday
        elif day_of_week == "5":
            airlines[unique_carrier, month][24] += 1 # count delays for Friday
            airlines[unique_carrier, month][25] += delayed_hours # count hours for delays on Friday
        elif day_of_week == "6":
            airlines[unique_carrier, month][26] += 1 # count delays for Saturday
            airlines[unique_carrier, month][27] += delayed_hours # count hours for delays on Saturday
        elif  day_of_week == "7":
            airlines[unique_carrier, month][28] += 1 # count delays for Sunday
            airlines[unique_carrier, month][29] += delayed_hours # count hours for delays on Sunday
    
    if(delayed_hours >= 15):
        if(carrier_delay.isdigit()):
            airlines[unique_carrier, month][30] += int(carrier_delay) # count minutes for carrier delay
            airlines[unique_carrier, month][31] += 1 if int(carrier_delay) > 0 else 0 # count carrier delays
        
        if(weather_delay.isdigit()):
            airlines[unique_carrier, month][32] += int(weather_delay) # count minutes for weather delay
            airlines[unique_carrier, month][33] += 1 if int(weather_delay) > 0 else 0 # count weather delays
        
        if(nas_delay.isdigit()):
            airlines[unique_carrier, month][34] += int(nas_delay) # count minutes for nas delay
            airlines[unique_carrier, month][35] += 1 if int(nas_delay) > 0 else 0 # count nas delays
        
        if(security_delay.isdigit()):
            airlines[unique_carrier, month][36] += int(security_delay) # count minutes for security delay
            airlines[unique_carrier, month][37] += 1 if int(security_delay) > 0 else 0 # count security delays
        
        if(late_aircraft_delay.isdigit()):
            airlines[unique_carrier, month][38] += int(late_aircraft_delay) # count minutes for late aircraft delay
            airlines[unique_carrier, month][39] += 1 if int(late_aircraft_delay) > 0 else 0 # count late aircraft delays
    
    if(cancelled == "1"):
        airlines[unique_carrier, month][40] += 1
    if(cancellation_code == "A"): # late aircraft delay
        airlines[unique_carrier, month][41] += 1
    
    if(cancellation_code == "B"): # weather delay
        airlines[unique_carrier, month][42] +=1
    
    if(cancellation_code == "C"): # nas delay
        airlines[unique_carrier, month][43] +=1
    
    if(cancellation_code == "D"): # security delay
        airlines[unique_carrier, month][44] +=1
    
    airlines[unique_carrier, month][45] += 1 # count total flights

# set max or min to None when there are no max or mins
for airline in airlines:
    if(airlines[airline][2] == sys.maxsize):
        airlines[airline][2] = None
    
    if(airlines[airline][3] == 0):
        airlines[airline][3] = None

writer = csv.writer(open(out_file, 'w', newline = ''))
writer.writerow(["AIRLINE", "MONTH", "DELAY_MINS_TOTAL", "TOTAL_DELAYS", "MIN_DELAY", "MAX_DELAY", "GRP_1_TOTAL", "GRP_2_TOTAL", "GRP_3_TOTAL", "GRP_4_TOTAL", "GRP_5_TOTAL", "GRP_6_TOTAL", "GRP_7_TOTAL", "GRP_8_TOTAL", "GRP_9_TOTAL", "GRP_10_TOTAL", "GRP_11_TOTAL", "GRP_12_TOTAL", "MON_TOTAL_DELAYS", "MON_HOURS_DELAY", "TUE_TOTAL_DELAYS", "TUE_HOURS_DELAY", "WED_TOTAL_DELAYS", "WED_HOURS_DELAY", "THU_TOTAL_DELAYS", "THU_HOURS_DELAY", "FRI_TOTAL_DELAYS", "FRI_HOURS_DELAY", "SAT_TOTAL_DELAYS", "SAT_HOURS_DELAY", "SUN_TOTAL_DELAYS", "SUN_HOURS_DELAY", "CARRIER_DELAY_MINS", "CARRIER_DELAY_TOTAL", "WEATHER_DELAY_MINS", "WEATHER_DELAY_TOTAL", "NAS_DELAY_MINS", "NAS_DELAY_TOTAL", "SECURITY_DELAY_MINS", "SECURITY_DELAY_TOTAL", "LATE_AIRCRAFT_DELAY_MINS", "LATE_AIRCRAFT_DELAY_TOTAL", "CANCELLED_TOTAL", "CANCELLATIONS_CARRIER", "CANCELLATIONS_WEATHER", "CANCELLATIONS_NAS", "CANCELLATIONS_SECURITY", "TOTAL_FLIGHTS"])
writer.writerows([airline[0]] + [airline[1]] + airlines[airline] for airline in airlines)
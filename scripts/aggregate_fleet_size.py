import csv, sys
from collections import defaultdict

def default_factory():
    return [0, 0, 0, 0] # intialize values

#file = '../data/tests/aggregate_airline_fleets.csv'7
#file = '../data/flights_delayed_cancelled/01jan.csv'
file = '../data/lookups/fleet_data.csv' # file to read from
out_file = '../data/lookups/fleet_data_totals.csv' # file to write to

reader = csv.DictReader(open(file, newline=''))
airline_fleets = defaultdict(default_factory)
for row in reader:
    # variables for fields read in
    airline = row["AIRLINE"]
    fleet_size = row["CURRENT"]
    average_age = row["AVERAGE_AGE"]
    
    if(fleet_size.isdigit()): # filters negative values
        fleet_size = int(fleet_size)
    else:
        fleet_size = 0
    
    if(average_age): # filters negative values
        average_age = float(average_age)
    else:
        average_age = 0
        
    if (average_age): # check for values
        airline_fleets[airline][1] += 1 # count averages
        
    airline_fleets[airline][0] += fleet_size # sum fleets
    airline_fleets[airline][2] += average_age # sum average ages
    

# set max or min to None when there are no max or mins
for airline in airline_fleets:
    if(airline_fleets[airline][2] and airline_fleets[airline][1]):
        airline_fleets[airline][3] = airline_fleets[airline][2]/airline_fleets[airline][1]

writer = csv.writer(open(out_file, 'w', newline = ''))
writer.writerow(["AIRLINE", "FLEET_SIZE", "AVERAGE_TOTALS", "AVERAGE_SUM", "AVERAGE_AGE"])
writer.writerows([airline] + airline_fleets[airline] for airline in airline_fleets)
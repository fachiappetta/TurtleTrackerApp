#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Francesca Chiappetta (fac16@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Ask user for the search date
user_date = input("Enter date to search for Sara: ")

# create a variable pointing to thje data file
file_name ="./data/raw/sara.txt"

#create a file object from the file
file_object = open(file_name, 'r')

#line read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

#create two empty dictionary objects id lc is 1,2,3,
date_dict = {}
coord_dict = {}


# Iterate through all lines in the line list
for lineString in line_list:
	if lineString[0] in ("#", "u"):
		continue

	# Use the split command to parse the items in lineString into a list object
	lineData = lineString.split()
	
	# Assign variables to specfic items in the list
	record_id = lineData[0]   # ARGOS tracking record ID
	obs_date = lineData[2]   # Observation date
	obs_lc = lineData[4]       # Observation Location Class
	obs_lat = lineData[6]     # Observation Latitude
	obs_lon = lineData[7]     # Observation Longitude
	
	# Print information
	if obs_lc in ("1","2","3"):
		date_dict[record_id] = obs_date
		coord_dict[record_id] = (obs_lat, obs_lon)

#create empty list to hold matching keys
matching_keys = []

# Check that at least one key was returned; tell the user if not.
if len(matching_keys) == 0:
    print ("No observations recorded for {}".format(user_date))
else:
	#loop through items in the the date_dict, and collect keys for matching ones
	for date_item in date_dict.items():
		#get the date of the item
		the_key, the_date = date_item
		#see if the date matches the user date
		if the_date == user_date:
			#if so,add the key to the list
			matching_keys.append(the_key)
			
	#reveal locations for each key in matching_keys
	for matching_key in matching_keys:
		obs_lat, obs_lon = coord_dict[matching_key]
		print(f"Record {matching_key} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {user_date}")
		
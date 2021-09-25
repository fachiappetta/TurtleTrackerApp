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

# create a variable pointing to thje data file
file_name ="./data/raw/sara.txt"

#create a file object from the file
file_object = open(file_name, 'r')

#line read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

#create two empty dictionary objects
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
	
	# Print information id lc is 1,2,3,
	if obs_lc in ("1","2","3"):
		print(f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
		date_dict[record_id] = obs_date
		coord_dict[record_id] = (obs_lat, obs_lon)




	###TASK 3
	





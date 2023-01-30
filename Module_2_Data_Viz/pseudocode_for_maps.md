# Preparing to Draw Maps
This document describes steps to follow **before** writing any code for the assignment of plotting cities on a map.

---

## Goal:
*It's helpful to summarize the main objective.*

- Plot city locations on a map.
	- Use circles as markers
	- Large (small) circles for warmer (cooler) temps
	- blue is cold, red is warm
	- Write temperature in circle

- We'll need to read a list of cities and temperatures from a data file.
		
---

## Project Workflow & Pseudocode:

**Before coding:** 
- Take a look at the mapping module.
	- Are there examples that will help me understand?  **If so, implement the example.**
	- Where is the documentation, so I'll know what options exist?
	- What is the basic flow for creating a map?
	- Is the module generating an output file?
	- Do I need to install anything?  (try to import)
- Similarly, look at the geocoding module.
- Am I going to write this as a Python script or a Jupyter notebook?
- Convert `.xls` to `.csv`.
	- Are there header rows to ignore?  If so, what is the delimiter?
		
---	

**Pseudocode**
*This is an outline of what my code will do...*

1. Import Modules:
	```
	csv 			# Needed to import spreadsheet

	geocoder? 		# Which module should I use?
	mapper? 		# Which module should I use?

	sys?  			# Am I using command-line args?
	math? 			# Is this necessary?
	```

2. We'll probably need to initialize our geocoder before we can geocode.
	
3. Import the .csv data (and geocode):	
	```
	open 'city_temperatures.csv' for reading
	for each row:
		if (this row does NOT start with the comment character):
			# Capture the information in this row:
			city = first column in this row (a string)
			state = second column in this row (a string)
			temp = third column in this row (a float)

			# Call the geocoder to get latitude and longitude:
			myLocString = a string of the form 'city, state'
			[lat, lon] = geocode(myLocString)
						
			# Save all of our information in a data structure.
			# Let's use a DICTIONARY of DICTIONARIES
			myData[i] = {
				'city': city, 
				'state': state, 
				'locString': myLocString,	(do we need to save this?)
				'temp': temp,
				'lat': lat,
				'lon': lon
			}
			# NOTES:  
			#	1) We need to initialize "myData" as a dictionary
			#	2) We need to do something with index "i"
	```

3. Capture some information to help us size/color the circle markers:
	```
	maxTemp = -infinity
	minTemp = +infinity
	for i in myData:
		if (myData[i]['temp'] > maxTemp):
			maxTemp = myData[i]['temp']
		if (myData[i]['temp'] < minTemp):
			minTemp = myData[i]['temp']		
	```

4. Specify a size and color for each circle marker:
	```
	# Set the size range (in pixels):
	coldestSize = 8		# pixels	
	hottestSize = 18 	# pixels
	for i in myData:
		myData[i]['circleSize'] = a value between coldestSize and hottestSize
		
	for i in myData:
		myData[i]['circleColor'] = a color along the red <--> blue spectrum
	```
	
5. Initialize an empty map:
	- We want our map to zoom appropriately to show all the markers.
	- *Do I need to specify a "center" location?  If so, what should I choose?*
	- *Or, can I specify a bounding box?*

6. Put markers on the map:
	*Since we're customizing marker size and color, and also adding text labels for temp, we'll need to do this one at a time*
	```
	for i in myData:
		# Draw a marker:
		location:	myData[i]['lat'], myData[i]['lon']
		size:		myData[i]['circleSize']
		color:		myData[i]['circleColor']
		
		# Add the temperature label:
		label:		myData[i]['temp']

		# Do I need to label the city?  Probably not if the city is already on the map.
	```
	
5. Show/Save the map.			
	
---

**Cleanup the code**
- Remove unnecessary print statements.
- Add/remove/edit comments.
	- Also copy/paste URLs for helpful Web pages.
- Watch for duplicated "for" loops.  Can we combine these to make the code more efficient?
- Are variable names descriptive?
- Have I left instructions for running the code?  Should I create a README file?
	
---
	
**Look for things to parameterize**
- What have I hardcoded?  Can/should these be parameterized?
- Should I use command-line arguments?	


	
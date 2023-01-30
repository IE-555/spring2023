# File:  LiveStream.py
#
# Be sure that this script is in the same directory
# as 'positive-words.txt' and 'negative-words.txt'
#
# How to Run:
# 1.  Search below for all instances of the word "FIXME".  
#     Follow the instructions for each FIXME item.
# 2.  From the command line, run
#     python LiveStream.py
# 3.  Hit CTRL-C to stop the script.
# 4.  Open osm.html in your Web browser to see a map of some tweets.
#
# ---------------------------------------------------------------------

import tweepy		# pip install tweepy		# FIXME -- May need to install.
import csv
import folium		# pip install folium		
import nltk			# http://nltk.org/			# FIXME -- May need to install.

# FIXME -- Provide search words/phrases:
# setTerms = ['enter', 'your', 'search', 'terms', 'here']
# setTerms = ['climate', 'change']
setTerms = ['corona', 'coronavirus', 'corona virus', 'covid'] 

# Specify a language, or set of languages:
setLang = ['en']

# Specify the location of the output file...
logFile = 'tmp.txt'
fileOut = open(logFile, "w")		# Open for *writing*

# Create a map of our tweet locations
mapFile = 'osm.html'
map_osm = folium.Map(location=[45.372, -121.6972], zoom_start=2)

# Import +/- Words
posWords = []
negWords = []
with open('positive-words.txt', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if (row[0][0] != '%'):
			posWords.append(str(row[0]))
        
with open('negative-words.txt', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if (row[0][0] != '%'):
			negWords.append(str(row[0]))
		
# ================================

			
# See https://dev.twitter.com/overview/api/entities-in-twitter-objects
class StreamListener(tweepy.StreamListener):		
	def on_status(self,tweet):
		
		# Make the variables global
		global numPos
		global numNeg
		global tweetWords

		# FIXME -- You may want to uncomment some of these lines to see the stream:
		# These print statements display information directly to the screen.
		# See https://dev.twitter.com/overview/api/entities-in-twitter-objects
		# print(tweet.text)
		# print(tweet.geo)
		# print(tweet.user.geo_enabled)
		# print(tweet.user.location)
		# print(tweet.created_at)
		# print(tweet.id)
		# print(tweet.geo)
		# print(tweet.author.screen_name)
		# print(tweet.source)
		# print(tweet.place)
		# print(tweet.place['bounding_box'])
		# print(tweet.user.geo_enabled)
		# print(tweet.user.time_zone)
		# print(tweet.user.location)
		# print(tweet.coordinates)
		
		
		# Split the tweet text into separate words
		myList = tweet.text.split()
		# myList = ['here', 'is', 'some', 'text']
		
		# Initialize some dummy counter variables:
		tmpPos = 0
		tmpNeg = 0
		
		# Loop over each word:
		for myWord in myList:
			# Convert each word to lower case:
			# Also, encode as utf-8
			# myWord = myWord.encode('utf-8').lower()
			# NOTE:  The utf-8 encoding made words look like
			#        b'something', which was messing up our 
			#        conditional below.
			myWord = myWord.lower()
			tweetWords.append(myWord)

			
			# For each word, see if it's positive or negative:
			if (myWord in posWords):
				tmpPos += 1
				numPos += 1
				# print("found positive")
			if (myWord in negWords):
				tmpNeg += 1
				numNeg += 1
				# print("found negative")
	
		# If the tweet contains GPS coordinates, let's place a pin on the map:
		if (tweet.coordinates != None):
			myLon = tweet.coordinates['coordinates'][0]		
			myLat = tweet.coordinates['coordinates'][1]	
			print("\t User at (%f,%f) -- %s" % (myLat, myLon, tweet.user.location))

			# Add a pin to the map, color-coded based on sentiment
			if (tmpPos > tmpNeg):
				pinColor = 'green'
			elif (tmpPos < tmpNeg):
				pinColor = 'red'
			else:
				pinColor = 'blue'
				
			folium.Marker([myLat,myLon], icon = folium.Icon(color = pinColor), popup = tweet.text).add_to(map_osm)

		# If the tweet contains a bounding box, let's draw it on the map:
		if (tweet.place != None):
			# print(tweet.place.bounding_box.coordinates[0])

			# Unfortunately, Twitter gives coordinates in lon, lat order.
			coords = []
			for i in range(0,len(tweet.place.bounding_box.coordinates[0])):
				coords.append([tweet.place.bounding_box.coordinates[0][i][1], tweet.place.bounding_box.coordinates[0][i][0]])

			# Color-code based on sentiment
			if (tmpPos > tmpNeg):
				color = 'green'
				fill_color = 'green'
			elif (tmpPos < tmpNeg):
				color = 'red'
				fill_color = 'red'
			else:
				color = 'blue'
				fill_color = 'blue'
			
			# print(coords)
			folium.Polygon(coords, color=color, fill_color=fill_color, weight=2.5, opacity=1, popup = tweet.text).add_to(map_osm)

		
		# This fileOut statement saves some info to the text file you specified 
		# at the top of this script. 
		# You may modify this statement to incorporate the data from the "print" 
		# statements provided above.
		fileOut.write(str(tweet.text.encode('utf-8')) + "+" + str(tweet.created_at) + "+" + str(tweet.id) + "+" + str(tweet.geo) + "+" + str(setTerms) +  "\n")
	

class main_loop():
	def __init__(self):

		print("Starting the code")
				
		# Go to http://dev.twitter.com and create an app. 
		# The consumer key and secret will be generated for you.
		consumer_key    = ''		# <--- FIXME:  Enter the key here
		consumer_secret = ''		# <--- FIXME:  Enter the secret here
		
		# After the step above, you will be redirected to your app's page.
		# Create an access token under the the "Your access token" section
		access_token        = ''		# <--- FIXME:  Enter the token here
		access_token_secret = ''		# <--- FIXME:  Enter the token secret here
		
		auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth1.set_access_token(access_token, access_token_secret)
		print("Access Code Validation a Success")

		l = StreamListener()
		streamer = tweepy.Stream(auth=auth1, listener=l)
		streamer.filter(track = setTerms, languages = setLang)
	

if __name__ == '__main__':
	try:
		numPos = 0
		numNeg = 0
		tweetWords = []
		main_loop()
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt")
		fileOut.close()
		map_osm.save(mapFile)
		print("See %s and %s" % (mapFile, logFile))
		
		print("\nFound %d Positive words and %d Negative words" % (numPos, numNeg))
			
		# Now, do some NLTK stuff:
		fdist = nltk.FreqDist(tweetWords)
		print("Frequency Distribution:")
		print(fdist.most_common(20))
		
		print("Bigrams:")
		myBigrams = list(nltk.bigrams(tweetWords))
		fdist = nltk.FreqDist(myBigrams)
		print(fdist.most_common(20))
	
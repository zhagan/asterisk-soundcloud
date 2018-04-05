#!/usr/bin/env python

# send trace backs to log file
from asterisk import agitb
agitb.enable(display = False, logdir = '/var/log/asterisk/')


# import our libs
import sys
import asterisk.agi
import soundcloud
import random
 
# initilize the agi stuff, and update the trackback to use our agi handle
agi = asterisk.agi.AGI()
agitb.enable(agi, display = False, logdir = '/var/log/asterisk/')

# get the number to lookup
try:
   client = soundcloud.Client(client_id="8381923c813162186cf2ef8bc7d4e9f3")
   genre = agi.get_variable("genre")
   searchVar = agi.get_variable('word')
   tracks = client.get('/tracks', q=searchVar, limit=9, filter='streamable')
   #create a couple of variables
   i = 1
   answer = -1
   #iterate thru the tracks given
   for t in tracks:
   #maybe I should break this up but there is a lot of formatting going on 
   		answer=int(agi.appexec('Flite', 'press '+str(i)+' for '+t.title.encode('utf-8').translate(None, '"')+',any'))-49
  		#answer=int(agi.appexec('Flite', 'press '+str(i)+',any'))
  		if answer > -1:
  			break
   	 	agi.verbose(t.title.encode('utf-8'))
   		i =i+1
   #agi.appexec('Flite',"enter your selection now"+',any')		
   #agi.appexec('Read',"selection",,1)
   #answer=int(agi.get_variable('selection'))
   if answer < 0:
   		answer=int(agi.wait_for_digit(5000))-1
   agi.verbose('number pressed '+str(answer))
   titleTemp = tracks[answer].title.encode('utf-8')
   userTemp = tracks[answer].user
   nameTemp = userTemp['username'].encode('utf-8')
   trackid = str(tracks[answer].id)
   track = client.get('/tracks/' + trackid + '/stream', allow_redirects=False)
   urlTemp = track.location
   agi.set_variable("artistname", nameTemp)
   agi.set_variable("songname", titleTemp.translate(None, '"',))
   agi.set_variable("urlname", urlTemp)
   agi.verbose(track.location)

   #my_var = agi.get_variable('MyVar')
except asterisk.agi.AGIException:
   agi.verbose('MyVar not set, exiting...', 3)
   agitb.handler()
   sys.exit(1)

# play a file
#agi.stream_file(track.location)

#my_word = 'icup'
# read my var to the user
# agi.say_alpha(my_var)
#agi.say_alpha(my_word)

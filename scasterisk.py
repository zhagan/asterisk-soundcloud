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
   zack = client.get('/users', user='zack hagan')
   zackid = str(zack.id)
   print zackid
   tracks = client.get('/users/' + zackid + '/tracks)
   ;tracks = client.get('/tracks', user='zack hagan')
   randomsong = random.choice(tracks)
   
   trackid = str(randomsong.id)
   track = client.get('/tracks/' + trackid + '/stream', allow_redirects=False)
   urlTemp = track.location
   agi.verbose(urlTemp)
   agi.set_variable("urlname", urlTemp)
   agi.verbose(track.location)

   my_var = agi.get_variable('MyVar')
except asterisk.agi.AGIException:
   agi.verbose('MyVar not set, exiting...', 3)
   agitb.handler()
   sys.exit(1)

# play a file
#agi.stream_file(track.location)

my_word = 'icup'
# read my var to the user
# agi.say_alpha(my_var)
agi.say_alpha(my_word)

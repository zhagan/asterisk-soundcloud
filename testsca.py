#!/usr/bin/env python

# send trace backs to log file
#from asterisk import agitb
#agitb.enable(display = False, logdir = '/var/log/asterisk/')


# import our libs
import sys
#import asterisk.agi
import soundcloud
import random
 
# initilize the agi stuff, and update the trackback to use our agi handle
#agi = asterisk.agi.AGI()
#agitb.enable(agi, display = False, logdir = '/var/log/asterisk/')

# get the number to lookup
client = soundcloud.Client(client_id="8381923c813162186cf2ef8bc7d4e9f3")
tracks = client.get('/tracks', q='zack hagan',limit=9)

artists = client.get('/users', q='charles butler')

#for a in artists:
#  print a.username

print artists[0].id
artistid = str(artists[0].id)

lctracks = client.get('/users/' + artistid + '/tracks')

for l in lctracks:
  print l.title

# tracks = client.get('/users/' + zackid + '/tracks')
# tracks = client.get('/tracks', q='zack hagan')
randomsong = random.choice(tracks)
#print randomsong.title
# print randomsong.user
   
trackid = str(randomsong.id)
track = client.get('/tracks/' + trackid + '/stream', allow_redirects=False)
urlTemp = track.location
#print track.location
#  agi.verbose(urlTemp)
#  agi.set_variable("urlname", urlTemp)
#  agi.verbose(track.location)
#  my_var = agi.get_variable('MyVar')
#except asterisk.agi.AGIException:
 #  agi.verbose('MyVar not set, exiting...', 3)
 #  agitb.handler()

# play a file
#agi.stream_file(track.location)

#my_word = 'icup'
# read my var to the user
# agi.say_alpha(my_var)
#agi.say_alpha(my_word)

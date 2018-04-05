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
   agi.stream_file('../custom/track-instructions')
  	
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

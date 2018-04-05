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

# start program to collect variable from args
# Read and ignore AGI environment (read until blank line)


agi.verbose("before reading args")


# get the number to lookup
try:
   
   #digitPressed = agi.get_result('200')
   #agi.verbose("digit pressed : "+str(digitPressed))   
   #my_var =int(agi.get_variable('digit'))
   #agi.say_number(my_var)
   my_var = agi.execapp('Read','digit,custom/search-by-track,2')
   agi.verbose("digit pressed "+str(my_var) 
except asterisk.agi.AGIException:
   agi.verbose('MyVar not set, exiting...', 3)
   agitb.handler()
   sys.exit(1)

#alphabet encoding
if my_var == 21:
   #agi.verbose("god dang it works")
   letter = "a"  
elif my_var == 22:
   letter = "b"
elif my_var == 23:
   letter = "c"
elif my_var == 31:
   letter = "d"
elif my_var == 32:
   letter = "e"
elif my_var == 33:
   letter = "f"
elif my_var == 41:
   letter = "g"
elif my_var == 42:
   letter = "h"
elif my_var == 43:
   letter = "i"
elif my_var == 51:
   letter = "j"
elif my_var == 52:
   letter = "k"
elif my_var == 53:
   letter = "l"
elif my_var == 61:
   letter = "m"
elif my_var == 62:
   letter = "n"
elif my_var == 63:
   letter = "o"
elif my_var == 71:
   letter = "p"
elif my_var == 72:
   letter = "q"
elif my_var == 73:
   letter = "r"
elif my_var == 74:
   letter = "s"
elif my_var == 81:
   letter = "t"
elif my_var == 82:
   letter = "u"
elif my_var == 83:
   letter = "v"
elif my_var == 91:
   letter = "w"
elif my_var == 92:
   letter = "x"
elif my_var == 93:
   letter = "y"
elif my_var == 94:
   letter = "z"
elif my_var == 99:
   letter = " "
elif my_var == 10:
   letter = "0"
elif my_var == 11:
   letter = "1"
elif my_var == 12:
   letter = "2"
elif my_var == 13:
   letter = "3"
elif my_var == 14:
   letter = "4"
elif my_var == 15:
   letter = "5"
elif my_var == 16:
   letter = "6"
elif my_var == 17:
   letter = "7"
elif my_var == 18:
   letter = "8"
elif my_var == 19:
   letter = "9"   
elif my_var:
   letter =""
   agi.stream_file('error') 
   
agi.set_variable('newLetter', letter)
agi.say_alpha(letter)

#agi.stream_file(error)	
   #letter = 'a'
# play a file
#agi.stream_file(track.location)

#my_word = 'icup'
# read my var to the user
# agi.say_alpha(my_var)
#agi.say_alpha(my_word)

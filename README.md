# asterisk-soundcloud
A telephone interface for the soundcloud API

This is a telephone interface I developed for soundcloud, this works with PBX in a Flash and possibly other flavors of Asterisk.

A user call the system and then can search Soundclouds extensive catalog with pagination. The system utilizes Google's voice to text API
and then searches upon the results. 

Along with SIP Client the Python script module needs to be present, and of course you gotta have SIP trunk to recieve calls from the outside

Tested with https://www.zoiper.com/ free SIP app

All prompts (wavs) needed to deploy this system are included.

I had deployed this for a few years starting in 2013 but eventually I let my registration expire, hopefully someone will find this useful some day

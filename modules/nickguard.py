#!/usr/bin/env python
"""
nickguard.py - Phenny Nick Guard Module
Copyright 2012, Brian J. Black
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
import random

nickguard_deadline = 0

def isBlanket(input):
   return input.host.lower() == 'blanket.users.whatnet.org'

def setDeadline():
   # Sets a deadline before which the user can respond "yes, i'd like my nick please"
   global nickguard_deadline
   nickguard_deadline = time.time() + 60

def pastDeadline():
   # Returns true iff past deadline
   return time.time() > nickguard_deadline









def onn(phenny, input):
   if isBlanket(input) and pastDeadline() == False:
      phenny.say(":(")

def ony(phenny, input):
   #print "ony called"
   #print "isBlanket() ==" + str(isBlanket(input))
   #print pastDeadline()
   if isBlanket(input) and pastDeadline() == False:
      print "should be changing nick now..."
      phenny.write(('NICK','blxbot' + str(random.randrange(1000,9999))))
#ony.commands = ['y']
ony.rule = r'y'
ony.priority = 'low'
#hurr.thread = False


def onquit(phenny, input):
   if isBlanket(input):
      phenny.write(('NICK','blanket'))
onquit.rule = r'(.*)'
onquit.event = 'QUIT'
onquit.priority = 'low'

def onpart(phenny, input):
   if isBlanket(input):
      phenny.write(('NICK','blanket'))
onpart.rule = r'(.*)'
onpart.event = 'PART'
onpart.priority = 'low'

def onjoin(phenny, input): 
   #phenny.say("Hello! Join detected.")
   #phenny.say(input.host)
   if isBlanket(input):
      setDeadline()
      phenny.say("Hello blanket! Would you like your nick (y/n)? (Please take it within 60 seconds.)")
onjoin.rule = r'(.*)'
onjoin.event = 'JOIN'
onjoin.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()

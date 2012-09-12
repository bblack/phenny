#!/usr/bin/env python
"""
hurr.py - Phenny hurr Module
Author: brian black
About: it durrs on hurr
"""

import random

def hurr(phenny, input): 
   phenny.say('durr')
hurr.rule = r'hurr'
hurr.priority = 'low'
hurr.thread = False

def robotwink(phenny, input):
   phenny.say(';]')
robotwink.rule = r';]'
robotwink.priority = 'low'
robotwink.thread = False

if __name__ == '__main__': 
   print __doc__.strip()

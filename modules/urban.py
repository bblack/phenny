#!/usr/bin/env python
"""
urban.py - Phenny Dictionary Module
Copyright 2009, Sebastian N. Fernandez
Modified 2012/07/29 by Brian J. Black
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import re
import urllib2
import urllib
import sys
from BeautifulSoup import BeautifulSoup

def get_def(word):
   url = 'http://www.urbandictionary.com/define.php?term=' + urllib.quote(word)
   html = urllib2.urlopen(url).read()
   soup = BeautifulSoup(html)
   entries_tbl = soup.find('table', {'id': 'entries'})
   if entries_tbl == None:
      return ("Found no entries for " + word)
   word_td = entries_tbl.find('td', {'class': 'word'})
   if word_td.find('a'):
      # If there are only approximate matches, site lists them as links to the proper page
      return ("Found no entries for " + word + ", but some were close.")
   ret_word = word_td.find(text=True).replace('\n', '')
   ret_def = entries_tbl.find('div', {'class': 'definition'}).findAll(text=True)
   ret_def = ' '.join(ret_def)
   ret_def = ret_def[:300]
   return (ret_word + ': ' + ret_def)
                                                   
def urban(phenny, input):
   word = ' '.join(input.groups()[1:])
   phenny.say(get_def(word))

      
urban.commands = ['ud']

if __name__ == '__main__': 
   #print __doc__.strip()
   words = sys.argv[1:]
   print get_def(' '.join(words))
   

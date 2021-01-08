# -*- coding: utf-8 -*-

import re
import time
import json
import sys
import random
import collections
from inspect import getmembers
from pprint import pprint

import urllib
from time import sleep
from bs4 import BeautifulSoup
from chromote import Chromote


def write_html (data, name = "log"):
    f = open (name+".htm","w")
    #print data
    f.write (data)
    f.close



def mt_rand (low = 0, high = sys.maxint):
    """Generate a better random value
    """
    return random.randint (low, high)


"""

"""
chrome = Chromote()
tab = chrome.tabs[0]
tab.set_url('http://bosslike.ru/tasks/instagram/like/')
time.sleep(.900) # Wait for 300 milliseconds
time.sleep(.900) # Wait for 300 milliseconds
time.sleep(.900) # Wait for 300 milliseconds
for dotask in range(11):
    print 'dotask: ' +  str(dotask)
    r = tab.evaluate('document.querySelectorAll("a.do-task")[' + str(dotask) + '].click()')
    print r

    """
    POP-UP
    """
    time.sleep(mt_rand(8,10))
    tab_popup = chrome.tabs[0]
    print 'chrome POP-UP: '
    print len(chrome)
    #[Chromote(tabs=2)]
    if len(chrome) == 1:
        continue
    
    #write_html(tab_popup.html)

    try:
        # Лайкнуть фотографию
        #r = tab_popup.evaluate('document.querySelector("button.coreSpriteHeartOpen").click()')
        r = tab_popup.evaluate('document.querySelectorAll("button[class*=wpO6b]")[1].click()')
        #tab_popup.evaluate('document.querySelector("a.fr66n span[class=ptsdu]").click()')
        print r
        
    except AttributeError:
        try:
            print 'except0'
            r= tab_popup.evaluate('document.querySelector("a.fr66n span[class=ptsdu]").click()')
            print r
        except AttributeError:
            print 'except1'

    time.sleep(mt_rand(8,8))
    time.sleep(.900) # Wait for 600 milliseconds
    chrome.close_tab(tab_popup)
    time.sleep(mt_rand(5,5))


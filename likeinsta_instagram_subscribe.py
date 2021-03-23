# -*- coding: utf-8 -*-

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


chrome = Chromote()
tab = chrome.tabs[0]
tab.set_url('https://likeinsta.ru/tasks/instagram/subscribe/')
time.sleep(.990) # Wait 
for dotask in range(11):
    print 'dotask: ' +  str(dotask)
    r = tab.evaluate('document.querySelectorAll("a.do-task")[' + str(dotask) + '].click()')
    print r

    """
    POP-UP
    """
    time.sleep(mt_rand(14,16))
    tab_popup = chrome.tabs[0]
    if len(chrome) == 1:
        continue
    #write_html(tab_popup.html)
    soup = BeautifulSoup(tab_popup.html, 'html5lib')

    try:
        tab_popup.evaluate("var element = document.querySelector('div.nZSzR button._5f5mN.jIbKX._6VtSN'); var o = document.createEvent('MouseEvents');o.initEvent('mousedown', true, true); element.dispatchEvent(o);")
        r = tab_popup.evaluate('document.querySelector("button._5f5mN.jIbKX._6VtSN").click()')
        print r
    except AttributeError:
        try:
            print 'except0'
        except AttributeError:
            print 'except1'

    time.sleep(mt_rand(3,5))
    time.sleep(.300) # Wait for 300 milliseconds
    chrome.close_tab(tab_popup)
    time.sleep(mt_rand(3,5))
    r = tab.evaluate('document.querySelector("a.do.btn").click()')
    time.sleep(mt_rand(2,3))

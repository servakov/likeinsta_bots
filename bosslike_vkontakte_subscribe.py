# -*- coding: utf-8 -*-

import os
import time
import string
import re
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


tab.set_url('http://bosslike.ru/tasks/vkontakte/subscribe/')
time.sleep(.300) # Wait for 300 milliseconds

for dotask in range(3):
    print 'dotask: ' +  str(dotask)
    #r = tab.evaluate('document.getElementsByClassName("do-task")[' + str(dotask) + '].click()')
    r = tab.evaluate('document.querySelectorAll("a.do-task")[' + str(dotask) + '].click()')
    print r

    """
    POP-UP

    """
    time.sleep(mt_rand(8,9)) # SmartLike Защита вашего профиля В социальных сетях существуют лимиты. Наш модуль SmartLike поможет вам работать аккуратней, не задумываясь о частоте выполнения заданий!
    all_tabs = chrome._get_tabs
    tab_popup = chrome.tabs[0]
    print 'chrome POP-UP: '
    #print len(chrome)
    print chrome
    #[Chromote(tabs=2)]
    if len(chrome) == 1:
        continue

    #write_html(tab_popup.html)
    soup = BeautifulSoup(tab_popup.html, 'html5lib')

    try:
        print 'Groups.enter:'
        btn3 = soup.find('button', {'id': 'join_button'}).get('onclick')
        #print btn3
        r = tab_popup.evaluate(btn3)
        print r
    except AttributeError:
        print 'Profile.toggleFriend:'
        r = tab_popup.evaluate('document.getElementsByClassName("profile_action_btn")[1].getElementsByTagName("button")[0].click()')
        print r
        try:

            print 'acceptFriendBtn!'
            r = tab_popup.evaluate('document.querySelectorAll("a.acceptFriendBtn")[0].click()')
            print r

        except AttributeError:
            print 'AttributeError=>Public.subscribe:'
            r = tab_popup.evaluate('Public.subscribe()')
            print r
        else: 
            print 'else: Public.subscribe:'
            r = tab_popup.evaluate('Public.subscribe()')

    time.sleep(mt_rand(6,7))
    chrome.close_tab(tab_popup)
    time.sleep(mt_rand(6,9))


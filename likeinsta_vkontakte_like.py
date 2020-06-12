# -*- coding: utf-8 -*-

import time
import json
import sys
import os
import string
import re
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
tab.set_url('https://likeinsta.ru/tasks/vkontakte/like/')
#time.sleep(.300) # Wait for 300 milliseconds
time.sleep(mt_rand(6,7))

for dotask in range(3):
    print 'dotask: ' +  str(dotask)
    r = tab.evaluate('document.querySelectorAll("a.do-task")[' + str(dotask) + '].click()')
    print r

    """
    POP-UP
    """
    time.sleep(mt_rand(6,7)) # SmartLike Защита профиля
    tab_popup = chrome.tabs[0]
    print 'chrome POP-UP: '
    print len(chrome)
    if len(chrome) == 1:
        continue
    write_html(tab_popup.html)
    try:
        print 'vkontakte Wall.likesShow: '
        soup = BeautifulSoup(tab_popup.html, 'html.parser')
        ahref3 = soup.find_all("a", { "class" : "like_btn"})
        '''
        for btn in ahref3:
            print btn.attrs
            #print btn
        '''
        print 'len(ahref3) Wall.likeIt: '
        print len(ahref3)
        if len(ahref3) > 0:
            r = tab_popup.evaluate('document.querySelectorAll("a.like_btn")[0].click()')
            print r

        else:
            div = soup.find_all("div", { "class" : "pv_like"})
            if len(div)>0:
                print 'ELSE Photoview.likeOver: '
                print 'len(div) Photoview.like: '
                print len(div)
                r = tab_popup.evaluate('document.querySelectorAll("div.pv_like")['+ str(len(div)-1) +'].click()')
                print r
            else:
                print 'ELSE Videoview.like: '
                btn4 = soup.find_all("button", { "class" : "mv_like_wrap"})
                """
                for btn in btn4:
                    print btn.attrs
                    #print btn
                """
                print 'len(btn4) Videoview.like: '
                print len(btn4)
                r = tab_popup.evaluate('document.querySelectorAll("button.mv_like_wrap")['+ str(len(btn4)-1) +'].click()')
                print r
    except AttributeError:
        try:
            print 'except0'
            r = tab_popup.evaluate('document.querySelector("a.item_like _i").click()')
            print r
        except AttributeError:
            print 'except1'

    time.sleep(.990) # Wait for 990 milliseconds
    chrome.close_tab(tab_popup)
    time.sleep(mt_rand(3,4))


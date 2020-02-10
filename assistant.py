import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import urllib
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
from time import strftime

class Assistant():
    
    def subReddit(self, command):
        reg_ex = re.search('open subreddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            print('opening r/' + subreddit + '...')
            url = url + 'r/'+ "".join(subreddit.split())
            webbrowser.open(url)
        else:
            print('whats the name of subreddit again?..')
    
    def openWebsite(self, command):
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            website = reg_ex.group(1)
            url = 'https://www.' + website
            print('opening ' + website + ' ...')
            webbrowser.open(url)
        else:
            print("please say the name of domain again")
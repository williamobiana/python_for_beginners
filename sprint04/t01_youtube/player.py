# Read the python webbrowser module documentation
# https://docs.python.org/3/library/webbrowser.html

# How to open a URL in the browser using the webbrowser module?
# How to make sure that a web page will open specifically in a new tab or window?
# What is the role of the BROWSER environment variable?
# Convenient Web-Browser Controller

# How to open a URL in the browser using the webbrowser module?
# import webbrowser
#
# webbrowser.open('https://www.youtube.com')
#
# -------------------------------------------
#
# import webbrowser as wb
# from random import randint
# 
# ran_num = [randint(0, 2100) for num in range(3)]
# 
# base_url = 'https://xkcd.com'
# 
# for num in range(3):
#     wb.open(f'{base_url}/{ran_num[num]}')


# How to make sure that a web page will open specifically in a new tab or window?
# import webbrowser
#
# webbrowser.open_new('https://www.youtube.com') #for new window
# webbrowser.open_new_tab('https://www.youtube.com') #for new tab


# What is the role of the BROWSER environment variable?
# to specify which browser to open with.
# https://www.tutorialspoint.com/convenient-web-browser-controller-in-python

# import webbrowser as browser
# my_browser = browser.get('windows-default')
# my_browser.open_new('http://www.tutorialspoint.com')

from helper import *
import webbrowser
import re
import sys #for commandline arguments
#https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

try:
    url = (sys.argv[1])
    url_pattern = 'https?://[\w]*.?[\w]+.[\w]*:?[0-9/]?'
    url_regex = re.search(url_pattern, url)

    if url_regex:
        try:
            if 'youtube' in url:
                print_stdout(f"Opening the YouTube video at {url}.")
                webbrowser.open(url)
                print_stdout(f"YouTube video opened.")
            else:
                print_stderr('The URL is invalid')
        except:
            print_stderr('The site URL format is invalid')
except:
    print_stderr('The site URL was not passed')

    
            


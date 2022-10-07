# What is a URL ?
# What elements does a URL consist of?
# What is the difference between standard error and standard output streams?
# How to create your own module in Python?
# What is a request (in programming)?
# How to make an HTTP request using the requests library?
# What HTTP methods are there?
# What is the result of an HTTP GET request?
# What status codes can a response have?
# How to get the content at a certain URL?


### What is a URL? ###
# URL stands for Uniform Resource Locator
# it is the address of a given unique resource on the Web.
# http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument


# scheme = http://
# authority = www.example.com:80
# path to resource = /path/to/myfile.html
# parameters = ?key1=value1&key2=value2
# anchor = #SomewhereInTheDocument


# What is the difference between standard error and standard output streams?
# The standard output stream is typically used for command output, 
# ... to display the results of a command to the user. 
# The standard error stream is typically used to display any errors that occur when a program is running.


# How to create your own module in Python?
# https://www.programiz.com/python-programming/modules
# https://www.analyticsvidhya.com/blog/2021/07/working-with-modules-in-python-must-known-fundamentals-for-data-scientists/#h2_6
# 
# The core idea of use modules is to minimize the code
# We can break a complete code into separate parts, add to a module. 
# and then we can call these modules in our main program logic.
# 
# example:
# nano mymodule.py 
# def welcome(name):
#   print("Hello, " + name +" to Analytics Classes")
# 
# in script
# import mymodule
# mymodule.welcome(william)
# # output: Hello william to Analytics Classes
# 
# or 
# 
# from mymodule import welcome
# welcome(william)
# # output: Hello william to Analytics Classes
#
# How to organize your code with modules and packages
# https://towardsdatascience.com/learn-python-modules-and-packages-in-5-minutes-bbdfbf16484e


# What is a request (in programming)?
# request–response or request–reply is one of the basic methods computers use to communicate with 
# .... each other in a network
# user request 'HTTP request message' to web server.
# web server reply 'HTTP respond message' to user.


# How to make an HTTP request using the requests library? 

## import requests module
# import requests

### r is for response. ###

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# >>> r.status_code
# 200
# >>> r.headers['content-type']
# 'application/json; charset=utf8'
# >>> r.encoding
# 'utf-8'
# >>> r.text
# '{"type":"User"...'
# >>> r.json()
# {'private_gists': 419, 'total_private_repos': 77, ...}

# What HTTP methods (response method) are there?
# https://www.geeksforgeeks.org/response-methods-python-requests/


# What is the result of an HTTP GET request?
# This is a request you send from your browser to view/read a page
# https://www.devopsforit.com/posts/what-is-rest-api-and-how-do-they-work

# What status codes can a response have?
# Here’s a quick overview of what each status code means:
#     1XX - Information
#     2XX - Success
#     3XX - Redirect
#     4XX - Client Error (you made an error)
#     5XX - Server Error (they made an error)

# How to get the content at a certain URL?
# response.json() (returns in json)
# response.content (returns in bytes)

#example
### import requests module
# import requests
#  
### Making a get request
# response = requests.get('https://api.github.com')
#  
### print response
# print(response)
#  
### print json content
# print(response.json())


import re
import requests
from helper import *

def html_save(url, file_path):

    # validates the URL using a validation regex
    
    # scheme = http://    ('^https?//')        
    # authority = www.example.com   ('[\w]*.?[\w]+.[\w]+')
    # port = :80   ('.?[0-9]*$')      
    # path to resource = /path/to/myfile.html
    # parameters = ?key1=value1&key2=value2
    # anchor = #SomewhereInTheDocument 

    url_regex = re.search('https?://[\w]*.?[\w]+.[\w]*:?[0-9/]?', url)

    if url_regex:
        try:
            print_stdout(f'Sending the request to {url}.')
            print_stdout(f'Request to {url} has been sent.')

            response = requests.get(url)
            with open(file_path, 'wb') as file:  #wb: write in binanry 
                file.write(response.content)
            print_stdout(f'<Response [{response.status_code}]>.')

            if response.status_code != int(200):
                message = 'Request failed'
                print_stderr(message)
            
            else:
                print_stdout(f'Parsing page data.')
                print_stdout(f'Page data has been parsed.')
                print_stdout(f'Saving page data to {file_path}.')
                print_stdout(f'Page data has been saved.')

        except:
            message = 'Request failed'
            print_stderr(message)   
        
    else:
        message = 'The site URL format is invalid'
        print_stderr(message)


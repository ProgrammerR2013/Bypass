#!/bin/python
# Import all the packages (you have to download coloroma, requests, and urllib3)
import requests
import sys
import coloroma import time
from coloroma import Fore, Style
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Setup stuff
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
domain = sys.argv[1]
path = sys.argv[2]
url = domain + path

# Opening screen 
print(
    Style.BRIGHT
    + Fore.BLUE
    + """
    ___    _______  ______    ______            _______  _______  _______  _______  _______  _______ 
   /   )  (  __   )/ ___  \  (  ___ \ |\     /|(  ____ )(  ___  )(  ____ \(  ____ \(  ____ \(  ____ )
  / /) |  | (  )  |\/   \  \ | (   ) )( \   / )| (    )|| (   ) || (    \/| (    \/| (    \/| (    )|
 / (_) (_ | | /   |   ___) / | (__/ /  \ (_) / | (____)|| (___) || (_____ | (_____ | (__    | (____)|
(____   _)| (/ /) |  (___ (  |  __ (    \   /  |  _____)|  ___  |(_____  )(_____  )|  __)   |     __)
     ) (  |   / | |      ) \ | (  \ \    ) (   | (      | (   ) |      ) |      ) || (      | (\ (   
     | |  |  (__) |/\___/  / | )___) )   | |   | )      | )   ( |/\____) |/\____) || (____/\| ) \ \__
     (_)  (_______)\______/  |/ \___/    \_/   |/       |/     \|\_______)\_______)(_______/|/   \__/
                                                                                                    
                                                                        By ProgrammerR_2013                                                                                              
    """

p

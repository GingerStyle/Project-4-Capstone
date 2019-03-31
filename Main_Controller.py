import requests
import requests_cache
from UI.py import *

#todo create cache for api responses
#todo divide up work between team members

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

class send_seasrch_to_api():
    #This class will send the search from UI.py to API_Manager.py

class retrieve_and_cache_results():
    #This class will receive the search results then cahce them

class save_search_results():
    #this class will take the search results and save them if the user would like
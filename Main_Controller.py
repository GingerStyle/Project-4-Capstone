import requests
import requests_cache
from UI.py import *

#todo create cache for api responses
#todo divide up work between team members

requests_cache.install_cache('search_param_cache', backend='sqlite')

class send_seasrch_to_api():
    #This class will send the search from UI.py to API_Manager.py
    



class retrieve_and_cache_results():
    #This class will receive the search results then cahce them
    search_criteria = search_param
    


class save_search_results():
    #this class will take the search results and save them if the user would like
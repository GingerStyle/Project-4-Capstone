import requests
from requests.exceptions import HTTPError

URL = 'http://ws.audioscrobbler.com/2.0/'

class LastFMAPI():

    #a function to query the api for concert dates
    def get_events(self, search_term, key):
        #setup parameters for the api query
        parameters = {'method': 'artist.gettopalbums','artist': {search_term}, 'app_key': {key}, 'format': 'json'}

        #request data from eventful.com
        try:
            response = requests.get(URL, params=parameters)
            #only raise error is certain response codes are returned
            #got this idea from https://realpython.com/python-requests/
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as ex:
            print(f'Other error: {ex}')
        else:
            return response

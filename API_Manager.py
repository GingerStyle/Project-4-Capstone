import os
import LastFM_API
import LastFM_Object
import Eventful_API
import Eventful_Object

#get environment variable api keys
LASTFM_KEY = os.environ.get('LastFMKey')
EVENTFUL_KEY = os.environ.get('EventfulKey')

#instantiate instances of APIs
lastfm_api = LastFM_API()
eventful_api = Eventful_API()

#variables to hold response data
LASTFM_RESPONSE = []
ENVENTFUL_RESPONSE = []

class API_Manager():

    #gets responses from APIs
    def get_search_results(self, search_term):
        LASTFM_RESPONSE = lastfm_api.get_events(search_term, LASTFM_KEY)
        EVENTFUL_RESPONSE = eventful_api.get_events(search_term, EVENTFUL_KEY)


    #creates objects to return to Main_Controller
    def create_eventful_objects(self, EVENTFUL_RESPONSE):
        events = ENVENTFUL_RESPONSE['event']
        #list to hold eventful objects
        eventful = []
        for event in events:
            #create object
            eventful_object = Eventful_Object
            #fill object with data
            eventful_object.event = event['title']
            eventful_object.place = event['city_name']
            eventful_object.venue = event['venue_name']
            eventful_object.date = event['start_time']
            #add object to list
            eventful.append(eventful_object)

        return eventful

    def create_lastfm_objects(self, LASTFM_RESPONSE):
        albums = LASTFM_RESPONSE['album']
        #list to hold LastFM objects
        lastfm = []
        for album in albums:
            #create object
            lastfm_object = LastFM_Object
            #fill object with data
            lastfm_object.name = album['name']
            lastfm_object.url = album['url']
            #add object to list
            lastfm.append(lastfm_object)

        return lastfm


#events = response['event']

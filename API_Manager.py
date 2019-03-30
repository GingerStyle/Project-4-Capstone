import os
import Spotify_API
import Spotify_Object
import Eventful_API
import Eventful_Object

SPOTIFY_KEY = os.environ.get('')
EVENTFUL_KEY = os.environ.get('EventfulKey')




#if no error send back top 3 concert dates
            events = response['event']
            #list of dictionary to hold concert dates
            concerts = []
            count = 0
            while count < 4:
                #dictionary to hold event data
                event_data = {'event_name': '','venue': '', 'date': ''}
                for event in events:
                    event_data{'event_name'} =

                    count += 1

            #return the top three concert dates
            return concerts
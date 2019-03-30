#object to hold concert information from eventful api response
class Eventful_Object:
    #initiator
    def __init__(self, event, place, venue, date,):
        self.event = event
        self.place = place
        self.venue = venue
        self.date = date
    #return string
    def __str__(self):
        return f'{self.event} is in {self.place} at {self.venue} on {self.date}'
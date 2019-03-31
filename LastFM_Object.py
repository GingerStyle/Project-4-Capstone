#object to hold Last.fm top album information
class LastFM_Object:

     #initializer
     def __init__(self, name, url):
         self.name = name
         self.url = url

     #return string
     def __str__(self):
         return f'Album: {self.name}  More Info: {self.url}'
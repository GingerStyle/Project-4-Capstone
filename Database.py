from peewee import *

db = SqliteDatabase('Spotify_DB')


class Spotify_DB_Class(Model):
    artist_name = CharField()
    album_name = CharField()
    album_url = CharField()
    event_title = CharField()
    event_city = CharField()
    Concert_Date_Times = DateTimeField()


    class Meta:
        database = db

    def __str__(self):
        return f'{self.album_name} {self.album_url} {self.event_title}  {self.event_city}    {self.Concert_Date_Times}\n'

db.connect()
db.create_tables([Spotify_DB_Class])

def save_record(artistName, albumName, url, event_name, event_city_arg, concert_dates_arg):
    spotify_record = Spotify_DB_Class(artist_name=artistName, album_name=albumName, album_url=url, event_title=event_name, event_city=event_city_arg,
                              Concert_Date_Times=concert_dates_arg)
    spotify_record.save()

def get_one(artist_name):
    search_artist = input("Enter the artists\' name")
    search_result = Spotify_DB_Class.select().where(Spotify_DB_Class.artist_name == search_artist)
    #for record in search_result:
        #print(record)
#def delete_artist(name, link, bio_arg, genre_arg, concert_dates_arg):
 #   artist_deleted = Artist.delete().where(Artist.artist_name == name, Artist.spotify_link == link,
#    Artist.bio == bio_arg, Artist.Genre == genre_arg, Artist.Concert_Dates == concert_dates_arg).execute()

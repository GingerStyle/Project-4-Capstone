from peewee import *

import Database

dbClass = Database


#sends data to the 'save_record' function in Database.py
def saved_output(artistName, albumName, link, bio_arg, genre_arg, concert_dates_arg):
    dbClass.save_record(artistName, albumName, link, bio_arg, genre_arg, concert_dates_arg)


def get_one(search_artist):
    artistName = dbClass.Spotify_DB_Class.artist_name
    event_select = dbClass.Spotify_DB_Class.select()
    search_result = event_select.where(artistName == search_artist)
    return search_result

def get_all():
    all_records = dbClass.Spotify_DB_Class.select()
    return all_records



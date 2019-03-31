from Main_Controller import *

class ask_for_input():

    search_param = input("Please enter a Group/Artist name: ")

class ask_to_continue():

    while True:       

        continue_searching = input("Would you like to do another search? y/n: ")

        while continue_searching.lower() not in ("y", "n"):

            continue_searching = input("Would you like to do another search? y/n: ")

        if continue_searching.lower() == "y":

            ask_for_input()

            artist_output = "The Artist " + artist_name + " is having concerts at " + concert_list + " and their albums are " + album_list)

            save_artist()

        if continue_searching.lower() == "n":

            break

class save_artist():

    saving_artist = input("Would you like to save the Group/Artist? y/n: ")

    while saving_artist.lower() not in ('y', 'n'):

        saving_artist = input("Would you like to save the Group/Artist? y/n: ")

    if saving_artist.lower() == "y":

        

    if saving_artist.lower() == "n":

def main():
    ask_to_continue()

main()
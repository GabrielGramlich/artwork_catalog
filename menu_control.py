from artist import Artist
from artwork import Artwork
from get_input import *

def display_menu():
    print() # useless command to have something in my method
    ##TODO Create display menu method


def create_artist():
    name, email = get_user_input_with_two('Please insert artist information.', 'Name: ', 'Email: ')
    #TODO verify artist not in database
    artist = Artist(name, email)
    database_control.create_artist(artist)


def create_artwork():
    artist, name, price = get_user_input_with_three('Please insert artwork information.', 'Artist: ', 'Name: ', 'Price: ')
    #TODO verify artist in database
    #TODO verify price is float
    artwork = Artwork(artist, name, price)
    database_control.create_artwork(artwork)


def search_artwork():
    name = get_user_input('What artist would you like to find works for?', 'Name: ')
    artworks = database_control.search_artwork(name)
    print(name + '\'s works:')
    for work in artworks:
        print(work)
    #TODO display artworks


def update_artwork():
    artist_name, artwork_name = get_user_input_with_two('What artist and piece would you like to update?', 'Artist name: ', 'Artwork name: ')
    #TODO verify both exist
    availability = get_user_input('What would you like to set the availability to?', 'Availability: ')
    database_control.update_artwork(artist_name, artwork_name, availability)


def delete_artwork(artwork):
    artist_name, artwork_name = get_user_input_with_two('What artist and piece would you like to update?', 'Artist name: ', 'Artwork name: ')
    #TODO verify both exist
    #TODO verify user wants to delete
    database_control.delete_artwork(artist_name, artwork_name)

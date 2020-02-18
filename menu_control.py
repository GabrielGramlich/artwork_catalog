from artist import Artist
from artwork import Artwork
from get_input import *

def create_artist():
    name, email = get_user_input_with_two('Please insert artist information.', 'Name: ', 'Email: ')
    exists = search_artist(name)
    if not exists:
        artist = Artist(name, email)
        database_control.create_artist(artist)


def create_artwork():
    artist, name, price = get_user_input_with_three('Please insert artwork information.', 'Artist: ', 'Name: ', 'Price: ')
    exists = search_artist(name)
    if not exists:
        artwork = Artwork(artist, name, price)
        database_control.create_artwork(artwork)
    #TODO verify price is float


def search_artwork():
    name = get_user_input('What artist would you like to find works for?', 'Name: ')
    artworks = database_control.search_artwork(name)
    #TODO verify result not blank
    display_works(artworks)


def display_works(artworks):
    print(name + '\'s works:')
    for work in artworks:
        print(work)


def update_artwork():
    artist_name, artwork_name = get_user_input_with_two('What artist and piece would you like to update?', 'Artist name: ', 'Artwork name: ')
    #TODO verify both exist
    availability_string = get_user_input('What would you like to set the availability to? Enter \'y\' or \'n\'', 'Availability: ')
    #TODO verify correct response
    availability = False
    if availability_string == 'y':
        availability = True
    database_control.update_artwork(artist_name, artwork_name, availability)


def delete_artwork(artwork):
    artist_name, artwork_name = get_user_input_with_two('What artist and piece would you like to update?', 'Artist name: ', 'Artwork name: ')
    #TODO verify both exist
    #TODO verify user wants to delete
    database_control.delete_artwork(artist_name, artwork_name)

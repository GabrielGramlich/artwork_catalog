from artist import Artist
from artwork import Artwork
from get_input import *

def create_artist():
    name, email = get_user_input_with_two('Please insert artist information.', 'Name: ', 'Email: ')
    exists = search_artist(name)
    if not exists:
        artist = Artist(name, email)
        database_control.create_artist(artist)
    else:
        print('Artist already exists')

def create_artwork():
    artist, name, price = get_user_input_with_three('Please insert artwork information.', 'Artist: ', 'Name: ', 'Price: ')
    while True:
        try:
            price = price - .1
            price = price + .1
            break
        except:
            price = input('Invalid price. Please enter a number. ')
    exists = search_artist(name)
    if exists:
        artwork = Artwork(artist, name, price)
        database_control.create_artwork(artwork)
    else:
        print('No artist with that name.')


def search_artwork():
    name = get_user_input('What artist would you like to find works for?', 'Name: ')
    artworks = database_control.search_artwork(name)
    if len(artworks) > 0:
        display_works(artworks)
    else:
        print("Artist has no artwork.")


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

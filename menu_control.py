from artist import Artist
from artwork import Artwork
import database_control
from get_input import *

def create_artist():
    name, email = get_user_input_with_two('Please insert artist information.', 'Name: ', 'Email: ')
    exists = database_control.search_artist(name)
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
    exists = database_control.search_artist(name)
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
    exists = database_control.search_artist(name)
    if exists:
        availability_string = get_user_input('What would you like to set the availability to? Enter \'y\' or \'n\'', 'Availability: ')
        while availability_string != 'y' and availability_string != 'n':
            availability_string = get_user_input('Invalid response. Enter \'y\' or \'n\'', 'Availability: ')
        availability = False
        if availability_string == 'y':
            availability = True
        database_control.update_artwork(artist_name, artwork_name, availability)
    else:
        print('No artist with that name.')


def delete_artwork(artwork):
    artist_name, artwork_name = get_user_input_with_two('What artist and piece would you like to update?', 'Artist name: ', 'Artwork name: ')
    exists = database_control.search_artist(name)
    if exists:
    #TODO verify user wants to delete
        if get_user_input('Are you sure you want to delete?', 'Enter \'y\' or \'n\': ') == 'y':
            database_control.delete_artwork(artist_name, artwork_name)
        else:
            print('Deletion cancelled.')
    else:
        print('No artist with that name.')

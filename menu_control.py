from artist import Artist
from artwork import Artwork

def display_menu():
    print() # useless command to have something in my method
    ##TODO Create display menu method


def get_user_input(instructions, input_command):
    print(instructions)
    choice = input(input_command)
    return choice


def get_user_input_with_two(instructions, input_command_one, input_command_two):
    print(instructions)
    choice_one = input(input_command_one)
    choice_two = input(input_command_one)
    return choice_one, choice_two


def get_user_input_with_three(instructions, input_command_one, input_command_two, input_command_three):
    print(instructions)
    choice_one = input(input_command_one)
    choice_two = input(input_command_one)
    choice_three = input(input_command_three)
    return choice_one, choice_two, choice_three


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

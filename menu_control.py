def display_menu():
    print() # useless command to have something in my method
    ##TODO Create display menu method


def get_user_input(instructions, input_command):
    print(instructions)
    choice = input(input_command)
    return choice


def get_user_input(instructions, input_command_one, input_command_two):
    print(instructions)
    choice_one = input(input_command_one)
    choice_two = input(input_command_one)
    return choice_one, choice_two


def get_user_input(instructions, input_command_one, input_command_two, input_command_three):
    print(instructions)
    choice_one = input(input_command_one)
    choice_two = input(input_command_one)
    choice_three = input(input_command_three)
    return choice_one, choice_two, choice_three


def create_artist(artist):
    print() # useless command to have something in my method
    ##TODO Create method to create artist
    ##      Calls database_control


def create_artwork(artwork):
    print() # useless command to have something in my method
    ##TODO Create method to create artwork
    ##      Calls database_control


def search_artwork(artist):
    print() # useless command to have something in my method
    ##TODO Create method to search artwork
    ##      Calls database_control


def update_artwork(artwork, availability):
    print() # useless command to have something in my method
    ##TODO Create method to update artwork
    ##      Calls database_control


def delete_artwork(artwork):
    print() # useless command to have something in my method
    ##TODO Create method to delete artwork
    ##      Calls database_control

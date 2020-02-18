from menu_control import *
from menu import Menu

def main():
	menu = create_menu()

	while True:
		choice = get_user_input('Enter \'m\' to view menu, or enter your choice.', 'What would you like to do? ')
		if choice == 'q':
			break
		else:
			call_for_choice(menu, choice)


def create_menu():
	menu = Menu()

	menu.add_option('c', '[C]reate artist', create_artist)
	menu.add_option('a', '[A]dd artwork', create_artwork)
	menu.add_option('s', '[S]earch artwork', search_artwork)
	menu.add_option('u', '[U]pdate artwork', update_artwork)
	menu.add_option('d', '[D]elete artwork', delete_artwork)

	return menu


def call_for_choice(menu, choice):
	if menu.is_valid(choice):
		function = menu.get_function(choice)
		function()
	elif choice == 'm':
		print(menu)
	else:
		print('Invalid selection. Please try again.')


main()
from menu_control import display_menu

def main():
	while True:
		print('Enter \'m\' to view menu, or enter your choice.')
		choice = input('What would you like to do? ')
		if choice == 'q':
			break
		else:
			call_for_choice(choice)


def call_for_choice(choice):
    print() # useless command to have something in my method
	##TODO Call appropriate method based on user choice


main()
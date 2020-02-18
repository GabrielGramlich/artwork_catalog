from menu_control import get_user_input

def main():
	while True:
		choice = get_user_input('Enter \'m\' to view menu, or enter your choice.', 'What would you like to do? ')
		if choice == 'q':
			break
		else:
			call_for_choice(choice)


def call_for_choice(choice):
    print() # useless command to have something in my method
	##TODO Call appropriate method based on user choice


main()
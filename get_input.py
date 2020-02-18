def get_user_input(instructions, input_command):
    print(instructions)
    choice = input(input_command).upper()
    return choice


def get_user_input_with_two(instructions, input_command_one, input_command_two):
    print(instructions)
    choice_one = input(input_command_one).upper()
    choice_two = input(input_command_one).upper()
    return choice_one, choice_two


def get_user_input_with_three(instructions, input_command_one, input_command_two, input_command_three):
    print(instructions)
    choice_one = input(input_command_one).upper()
    choice_two = input(input_command_one).upper()
    choice_three = input(input_command_three).upper()
    return choice_one, choice_two, choice_three



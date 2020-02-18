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



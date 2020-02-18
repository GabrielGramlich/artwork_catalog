# NOTE TO CLARA
# This is essentially just the class used by you in readinglist, with the to string method modified for my own readability.
#  Repeating it so I can better understand how it works/how to implement it.

class Menu:


	def __init__(self):
		self.descriptions = {}
		self.functions = {}


	def add_option(self, key, description, function):
		self.descriptions[key] = description
		self.functions[key] = function


	def is_valid(self, choice):
		return choice in self.text_descriptions


	def get_action(self, choice):
		return self.functions.get(choice)


	def __str__(self):
		menu_choices = ''
		for key in self.descriptions.keys():
			menu_choices = menu_choices + str(key) + ': ' + self.descriptions[key] + '\n'
		return menu_choices

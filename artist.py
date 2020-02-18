class Artist:

	def __init__(self, name, email):
		self.name = name
		self.email = email


	def __str__(self):
		artist_info = 'Artist Information:\nName:\t' + self.name + '\nEmail:\t' + self.email + '\n'
		return artist_info

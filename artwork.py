class Artwork:

	def __init__(self, artist, name, price, availability):
		self.artist = artist
		self.artwork_name = name
		self.price = price
		self.availability = availability


	def __str__(self):
		artist_info = 'Artwork Information:\nArtist:\t\t' + self.artist + '\nName:\t\t' + self.artwork_name + '\nPrice:\t\t' + str(self.price) + 'Available:\t' + str(self.availability) + '\n'
		return artist_info

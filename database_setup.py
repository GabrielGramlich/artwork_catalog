from peewee import *

db = SqliteDatabase('artwork_catalog.sqlite')


class Artist_Table(Model):
    self.name = CharField()
    self.email = CharField()

    class Meta:
        database = db


    def __str__(self):
        return f'Artist:\t{self.name}\nEmail:\t{self.email}\n'


class Artwork_Table(Model):
    self.artist = CharField()
    self.artwork = CharField()
    self.price = DecimalField()
    self.availability = BooleanField()

    class Meta:
        database = db


    def __str__(self):
        return f'Artist:\t\t{self.name}\nArtwork:\t\t{self.artwork}\nPrice:\t\t{self.price}\nAvailability:\t{self.availability}\n'


db.connect()
db.create_tables([Artist_Table, Artwork_Table])

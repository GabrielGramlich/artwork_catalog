from peewee import *

db = SqliteDatabase('artwork_catalog.sqlite')

class Artist_Table(Model):
    artist_name = CharField()
    email = CharField()

    class Meta:
        database = db


    def __str__(self):
        return f'Artist:\t{self.artist_name}\nEmail:\t{self.email}\n'


class Artwork_Table(Model):
    artist = ForeignKeyField(Artist_Table.artist_name, backref='artist_name')
    artwork = CharField()
    price = DecimalField()
    availability = BooleanField()

    class Meta:
        database = db


    def __str__(self):
        return f'Artwork:\t{self.artwork}\nPrice:\t\t{self.price}\nAvailability:\t{self.availability}\n'


def setup():
    db.connect()
    db.create_tables([Artist_Table, Artwork_Table])
    db.close()

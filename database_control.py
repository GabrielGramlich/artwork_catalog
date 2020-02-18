from peewee import *
from database_setup import Artist_Table as Artist, Artwork_Table as Artwork

db = SqliteDatabase('artwork_catalog.sqlite')

def create_artist(artist):
    db.connect()
    artist = Artist(artist.name, artist.email)
    artist.save()
    db.close()


def create_artwork(artwork):
    print() # Useless line to have something in my method
    ##TODO Create add artwork method - create artist if not in database


def search_artwork(name):
    print() # Useless line to have something in my method
    ##TODO Create search artwork method by artist


def update_artwork(artist_name, artwork_name, availability):
    print() # Useless line to have something in my method
    ##TODO Create delete artwork method


def delete_search(artist_name, artwork_name):
    print() # Useless line to have something in my method
    ##TODO Create update availability status method

from peewee import *
from database_setup import Artist_Table as Artist, Artwork_Table as Artwork

db = SqliteDatabase('artwork_catalog.sqlite')

def create_artist(artist):
    db.connect()
    artist = Artist(artist.name, artist.email)
    artist.save()
    db.close()


def create_artwork(artwork):
    db.connect()
    artwork = Artwork(artwork.artist, artwork.name, artwork.price, artwork.availability)
    artwork.save()
    db.close()


def search_artwork(name):
    results = []
    db.connect()
    artist_work = Artwork().select().where(Artwork.artist == name)
    for work in artist_work:
        results.append(work)
    db.close()
    return results


def update_artwork(artist_name, artwork_name, availability):
    db.connect()
    Artwork().update(availability == availability).where(Artwork.artist == artist_name and Artwork.name == artist_name).execute()
    db.close()


def delete_search(artist_name, artwork_name):
    print() # Useless line to have something in my method
    ##TODO Create update availability status method

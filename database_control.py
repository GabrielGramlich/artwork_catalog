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


def search_artist(name):
    exists = False
    db.connect()
    artist = Artist().select().where(Artist.name == name)
    if len(artist) > 0:
        exists = True
    return exists


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
    rows_updated = Artwork().update(availability == availability).where(Artwork.artist == artist_name and Artwork.name == artist_name).execute()
    if rows_updated > 0:
        print('Successful update!')
    db.close()


def delete_search(artist_name, artwork_name):
    db.connect()
    rows_deleted = Artwork().delete().where(Artwork.artist == artist_name and Artwork.name == artist_name).execute()
    if rows_deleted > 0:
        print('Successful deletion!')
    db.close()

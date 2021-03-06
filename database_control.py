from peewee import *
from database_setup import Artist_Table as Artist, Artwork_Table as Artwork

db = SqliteDatabase('artwork_catalog.sqlite')

def create_artist(new_artist):
    db.connect()
    artist = Artist(artist_name=new_artist.name, email=new_artist.email)
    artist.save()
    db.close()


def create_artwork(new_artwork):
    db.connect()
    artwork = Artwork(artist=new_artwork.artist, artwork=new_artwork.artwork_name, price=new_artwork.price, availability=new_artwork.availability)
    artwork.save()
    db.close()


def search_artist(name):
    exists = False
    db.connect()
    artist = Artist().select().where(Artist.artist_name == name)
    if len(artist) > 0:
        exists = True
    db.close()
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
    rows_updated = Artwork().update(availability=availability).where(Artwork.artist == artist_name and Artwork.artwork == artwork_name).execute()
    if rows_updated > 0:
        print('Successful update!')
    else:
        print('Unable to update. Please check if piece exists.')
    db.close()


def delete_artwork(artist_name, artwork_name):
    db.connect()
    rows_deleted = Artwork().delete().where(Artwork.artist == artist_name and Artwork.artwork == artwork_name).execute()
    if rows_deleted > 0:
        print('Successful deletion!')
    else:
        print('Unable to delete. Please check if piece exists.')
    db.close()

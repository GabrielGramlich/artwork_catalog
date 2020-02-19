from peewee import *
import unittest
from database_setup import Artist_Table as Artist, Artwork_Table as Artwork

MODELS = [Artist, Artwork]

test_db = SqliteDatabase(':memory:')

class base_test_case(unittest.TestCase):

	def set_up(self):
		test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

		test_db.connect()
		test_db.create_tables(MODELS)

	def tear_down(self):
		test_db.drop_tables(MODELS)

		test_db.close()


if __name__ == '__main__':
    unittest.main()

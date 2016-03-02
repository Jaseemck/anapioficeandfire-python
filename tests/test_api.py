import datetime
from anapioficeandfire import cursor

try:
    from tests.configuration import AnApiOfIceAndFireTestCase
except:
    from configuration import AnApiOfIceAndFireTestCase

class AnApiOfIceAndFireTests(AnApiOfIceAndFireTestCase):
    def test_get_books(self):
        pages = list(cursor.Cursor(self.api.get_books).pages())

        self.assertGreater(len(pages), 1)

    def test_get_books_with_page_limit_of_one(self):
        pages = list(cursor.Cursor(self.api.get_books).pages(limit=1))

        self.assertEquals(len(pages), 1)

    def test_get_books_with_name(self):
        for page in cursor.Cursor(self.api.get_books, name='A Game of Thrones').pages():
            for book in page:
                self.assertEquals('A Game of Thrones', book.name)

    def test_get_books_with_from_release_date(self):
        release_date = '2015-1-1'
        for page in cursor.Cursor(self.api.get_books, from_release_date=release_date).pages():
            for book in page:
                self.assertGreater(book.released, release_date)

    def test_get_books_with_to_release_date(self):
        release_date = '2000-1-1'

        for page in cursor.Cursor(self.api.get_books, to_release_date=release_date).pages():
            for book in page:
                self.assertLess(book.released, release_date)

    def test_get_book(self):
        game_of_thrones = self.api.get_book(id=1)
        self.assertEquals(game_of_thrones.name, 'A Game of Thrones')

    def test_get_book_characters(self):
        game_of_thrones = self.api.get_book(id=1)

        first_character = game_of_thrones.get_characters().items(limit=1)

        self.assertIsNotNone(first_character)

    def test_get_book_pov_characters(self):
        game_of_thrones = self.api.get_book(id=1)
        number_pof_pov_characters = len(list(game_of_thrones.get_pov_characters().items()))
        self.assertEquals(9, number_pof_pov_characters)

    def test_get_character(self):
        jon_snow = self.api.get_character(id=583)
        self.assertEquals(jon_snow.name, 'Jon Snow')

    def test_get_character_allegiances(self):
        catelyn_stark = self.api.get_character(id=232)
        number_of_allegiances = len(list(catelyn_stark.get_allegiances().items()))
        self.assertEquals(2, number_of_allegiances)

    def test_get_character_books(self):
        catelyn_stark = self.api.get_character(id=232)
        number_of_books = len(list(catelyn_stark.get_books().items()))
        self.assertGreater(number_of_books, 0)

    def test_get_character_pov_books(self):
        catelyn_stark = self.api.get_character(id=232)
        number_of_pov_books = len(list(catelyn_stark.get_pov_books().items()))
        self.assertEquals(3, number_of_pov_books)

    def test_get_house(self):
        house_targaryen = self.api.get_house(id=378)
        self.assertEquals(house_targaryen.name, 'House Targaryen of King\'s Landing')

    def test_get_house_current_lord(self):
        house_baelish = self.api.get_house(id=10)
        current_lord = house_baelish.get_current_lord()

        self.assertEquals('Petyr Baelish', current_lord.name)

    def test_get_house_heir(self):
        house_tarly = self.api.get_house(id=379)
        heir = house_tarly.get_heir()

        self.assertEquals('Dickon Tarly', heir.name)

    def test_get_house_overlord(self):
        house_tarly = self.api.get_house(id=379)
        overlord = house_tarly.get_overlord()

        self.assertEquals('House Tyrell of Highgarden', overlord.name)

    def test_get_house_founder(self):
        house_stark = self.api.get_house(id=362)
        founder = house_stark.get_founder()

        self.assertEquals('Brandon Stark', founder.name)


    def test_get_house_cadet_branches(self):
        house_kenning = self.api.get_house(id=218)
        number_of_cadet_branches = len(list(house_kenning.get_cadet_branches().items()))

        self.assertGreater(number_of_cadet_branches, 0)

    def test_get_house_sworn_members(self):
        house_kenning = self.api.get_house(id=218)
        number_of_sworn_members = len(list(house_kenning.get_sworn_members().items()))

        self.assertGreater(number_of_sworn_members, 0)

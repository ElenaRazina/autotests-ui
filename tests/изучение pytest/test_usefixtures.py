import pytest

@pytest.fixture
def clear_books_database()->None:
    print("[FIXTURE] Очищаем базу книг")


@pytest.fixture
def fill_books_database()->None:
    print("[FIXTURE] Заполняем базу книгами ")
#Фикстуры ниего не возвращают, поэтому None

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Reading all books")

@pytest.mark.usefixtures('clear_books_database','fill_books_database')
class TestLibrary:
    def test_read_book_from_library(self):
        print("To read all books")

    def test_delete_book_from_library(self):
        print("Delete all books")
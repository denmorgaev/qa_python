import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection

'''Для корректного отображения аргументов в параметризированном тесте'''
def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def collection_five_books(collection):
    collect = collection
    books = ['Властелин колец', 'Король лев', 'Чужой', 'Сон в летнюю ночь', 'Молчание ягнят']
    genre = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect
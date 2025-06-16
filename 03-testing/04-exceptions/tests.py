import pytest 
from book import Book


@pytest.mark.parametrize('title,isbn',[("hallow","978-1779501127")])
def test_valid_creation(title,isbn):
    book = Book(title,isbn)
    assert book.isbn == isbn and book.title == title

@pytest.mark.parametrize('title,isbn',[("","978-1779501127")])
def test_book_creation_invalid_title(title,isbn):
    with pytest.raises(RuntimeError):
        book = Book(title,isbn) 

@pytest.mark.parametrize('title,isbn',[("harry","978-1701127"),("harry","978-177950112")])
def test_book_creation_invalid_isbn(title,isbn):
    with pytest.raises(RuntimeError):
        book = Book(title,isbn) 
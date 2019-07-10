class Author:
    def __init__(self, author_id, first_name, last_name, email, phone, address):
        self.author_id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return "Author ID: {0}, First name: {1}, Last name: {2}, Email: {3}, Phone: {4}, Address: {5}/////" \
            .format(self.author_id, self.first_name, self.last_name, self.email, self.phone, self.address)


class Book:
    def __init__(self, book_id, title, ibsn, publish_year, genres, views, votes, downloads, status, created_date,
                 uploaded_date,
                 list_authors=[]):
        self.book_id = book_id
        self.status = status
        self.created_date = created_date
        self.uploaded_date = uploaded_date
        self.title = title
        self.ibsn = ibsn
        self.publish_year = publish_year
        self.list_authors = list_authors
        self.genres = genres
        self.views = views
        self.votes = votes
        self.downloads = downloads

    def add_authors(self, item):
        if not self.list_authors:
            self.list_authors = []
        self.list_authors.append(item)

    def __repr__(self):
        return "Title: {0}, IBSN: {1}, Publish year: {2}, Genres: {3}, Views: {4}, Votes: {5}, Downloads: {6}, " \
               "Status: {7}, Created date: {8}, Uploaded date: {9}, Authors: {10}" \
            .format(self.title, self.ibsn, self.publish_year, self.genres, self.views, self.votes, self.downloads,
                    self.status, self.created_date, self.uploaded_date, self.list_authors)


class BookAuthorMapping:
    def __init__(self, book_id, author_id):
        self.book_id = book_id
        self.author_id = author_id


class Genres:
    def __init__(self, genres):
        self.genres = genres

    def __repr__(self):
        return "{}".format(self.genres)


class Status:
    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return "{}".format(self.status)


_status1 = Status("Published")
_status2 = Status("Not published")

_genres1 = Genres("Scary")
_genres2 = Genres("Sci-fi")
_genres3 = Genres("Romance")
_genres4 = Genres("Thriller")
_genres5 = Genres("Biography")

_author1 = Author("A1", "John", "Sankbeil", "John@email.com", "0903748273", "36 Lake View")
_author2 = Author("A2", "Jay", "Linehan", "Jay@email.com", "0903746284", "35 Lake View")
_author3 = Author("A3", "Mike", "Schneider", "Mike@email.com", "0903827364", "34 Lake View")
_author4 = Author("A4", "Richard", "Dudek", "Richard@email.com", "0903837492", "33 Lake View")
_author5 = Author("A5", "Edwin", "Ballines", "Edwin@email.com", "0903645285", "32 Lake View")

_list_books = [
    Book("B1", "HF57", 2005, _genres1, 37994, 37, 2677, _status1, "13/06/2009", "23/07/2011", [_author1, _author3]),
    Book("B2", "HG87", 2008, _genres3, 26482, 28, 3728, _status2, "15/03/2008", "26/07/2012", [_author1, _author5]),
    Book("B3", "HJ83", 2006, _genres2, 72945, 74, 2947, _status1, "12/06/2010", "04/02/2013", [_author2, _author4]),
    Book("B4", "HY68", 2007, _genres4, 29476, 22, 2445, _status2, "21/05/2008", "18/02/2010", [_author5, _author2]),
    Book("B5", "HI93", 2006, _genres5, 37254, 23, 7263, _status1, "29/04/2011", "06/02/2012", [_author1, _author2])
]

_mapping = [
    BookAuthorMapping(0, 1)
]


def get_books_of_author(list_book, author_id):
    book_ids = []
    for m in _mapping:
        if m.author_id == author_id:
            book_ids.append(m.book_id)

    rs = []
    for book in list_book:
        if book.book_id in book_ids:
            rs.append(book)

    return rs


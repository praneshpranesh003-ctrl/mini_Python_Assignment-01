def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("Available Books:")
    for book_id in catalog:
        if book_id not in borrowed_books:
            print(book_id, catalog[book_id])


catalog = {}
borrowed_books = []
members = set()

add_book(catalog, 1, "Python", "John", 2020)
add_book(catalog, 2, "Java", "Alice", 2021)
add_book(catalog, 3, "C++", "Bob", 2019)
add_book(catalog, 4, "AI", "David", 2023)

register_member(members, 101)
register_member(members, 102)
register_member(members, 103)
register_member(members, 101)

borrow_book(catalog, borrowed_books, 1)
borrow_book(catalog, borrowed_books, 3)

return_book(borrowed_books, 1)

show_available(catalog, borrowed_books)
def check_if_new(book, library):

    if book not in library:
        return True
    return False




def update_library(books, library):
 # '''
 # Input:  List - book names, Set - books already in library
 # Output: List - books that weren't in the library
 # '''
 new_books = []
 for book in books:
     if check_if_new(book, library) is True:
         print('The book, {} is new!'.format(book))
         new_books.append(book)
     library.add(book)
 print library
 return new_books

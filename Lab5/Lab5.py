"""
Application Name: Lab5.py
Developer: Alfred Varghese Jose
Date: 10/09/2023

An application program for a Library, where the users can add new books, display the existing books, search for a book and remove books from the library. 
"""

import pickle
import os


# add books to library
def library_add():

    if os.path.exists("library.dat"):
        library_file = open("library.dat", "rb")
        library = pickle.load(library_file)
        library_file.close()
        print("There may be one or more books in library .. .. .. ..")
    else:
        print("File does not exist. Creating a new file and adding book .. ..")
        library = {}

    book_title = input("\nEnter title of book:\t")
    book_author = input("\nEnter author of book :\t")
    book_price = float(input("\nEnter price of book:\t$"))
    book_isbn = input("\nEnter 9-digit ISBN of the book:\t")
    while True:
        if book_isbn.isdigit() and len(book_isbn) == 9:
            break
        else:
            print("\nInvalid ISBN Number .. .. .. ..")
            book_isbn = input("\nEnter book ISBN number ... a 9-charecters, numeric string:\t")

    book = []
    book.append(book_title)
    book.append(book_author)
    book.append(book_price)
    book.append(book_isbn)

    if library:
        print("Checking for the book in library based on ISBN .. ..")
        if book_isbn in library:
            print("Book already in Library .. .. New book cannot be added .. ..")
        else:
            print("Book is not in the Library .. .. Adding new book .. ..\nBook added to library stock .. .. ..")
            library[book_isbn] = book
    else:
        library[book_isbn] = book

    library_file = open("library.dat", "wb")
    pickle.dump(library, library_file)
    library_file.close()


# display library stock
def library_display():
    
    if os.path.exists("library.dat"):
        library_file = open("library.dat", "rb")
        library = pickle.load(library_file)
        library_file.close()

        if library:
            author_display()
            print("\n%60s\n%s" % ("Library", "#*"*60))
            print("\n%30s%30s%30s%30s" % ("Book's Title", "Book's Author", "Book Price", "ISBN"))
            for book in library.values():
                print("\n%30s%30s%30s%30s" % (book[0], book[1], "$%.2f" % book[2], book[3]))
            print("#*"*60)
        else:
            print("Library may not have books yet! .. .. ..")
    else:
        print("Library may not have books yet! .. .. ..")


# display author info
def author_display():

    print("\n%s\n%120s\n%120s\n%s" % ("#*"*60, "Alfred Varghese Jose", "N01619463","#*"*60))


# search for book in the library
def library_search():

    if os.path.exists("library.dat"):
        library_file = open("library.dat", "rb")
        library = pickle.load(library_file)
        library_file.close()

        if library:
            book_isbn = input("\nEnter ISBN number of book to search:\t")
            if book_isbn in library:
                author_display()
                print("\n%60s\n%s" % ("Library", "#*"*60))
                print("\n%30s%30s%30s%30s" % ("Book's Title", "Book's Author", "Book Price", "ISBN"))
                print("\n%30s%30s%30s%30s" % (library[book_isbn][0], library[book_isbn][1], "$%.2f" % library[book_isbn][2], library[book_isbn][3]))
                print("#*"*60)
            else:
                print(f"ISBN {book_isbn} is not available in Library .. .. ..")
        else:
            print("Book cannot be searched as there are no books in the Library .. .. ..")
    else:
        print("Book cannot be searched as there are no books in the Library .. .. ..")


# remove an book from library
def library_remove():
    
    if os.path.exists("library.dat"):
        library_file = open("library.dat", "rb")
        library = pickle.load(library_file)
        library_file.close()

        if library:
            book_isbn = input("\nEnter ISBN of book to remove:\t")
            if book_isbn in library:
                print("Book is in library - removing the book now .. .. ..")    
                library.pop(book_isbn)

                library_file = open("library.dat", "wb")
                pickle.dump(library, library_file)
                library_file.close()
            else:
                print(f"The book with ISBN number {book_isbn} is not in library - cannot be removed .. .. ..")
        else:
            print("There are no books to remove from the library .. .. ..")
    else:
        print("There are no books to remove from the library .. .. ..")


if __name__ == '__main__':

    print(__doc__)
    
    choice = ""

    # display menu and accept choice
    while True:

        print("\n\ta) Type 'Add' to add a book \n\tb) Type 'Display' to display books \n\tc) Type 'Search' to search book \n\td) Type 'Remove book' to remove book \n\te) Type 'End' to end the application \n")
        choice = (input("Enter your choice ... ...")).lower()
        
        if choice == 'add' or choice == 'a':
            library_add()

        elif choice == 'display' or choice == 'b':
            library_display()

        elif choice == 'search' or choice == 'c':
            library_search()

        elif choice == 'remove book' or choice == 'd':
            library_remove()

        elif choice == 'end' or choice == 'e':
            print("\nApplication ending now .. .. .. ..")
            break

        else:
            print("\nPlease enter a valid choice from the menu .. .. ..")
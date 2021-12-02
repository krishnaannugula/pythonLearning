# class library needs 3 methods displaybooks, lend a book and add a book
# class customer need request a book ro return a book


class Library:
    #availableBooks = ["Comic","English","Finnish"]
    

    def __init__(self, bookslist):
        self.availableBooks = bookslist
        #print(bookslist)

    def displaybooks(self):
        print()
        print("Avaiable books:")
        for books in self.availableBooks:
            print(books)
           


    def lendabook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("you have borrowed the book ",requestedBook)
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the request book is not available")

        
        

    def addabook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned the book",returnedBook, "Thank you!")


class Customer:
    def requestabook(self):
        print("enter the book you would like to brrow:")
        self.book = input()
        return self.book


        
    def returnabook(self):
        print("enter the name of the book")
        self.book = input()
        return self.book





library= Library(["Comic","English","Finnish"])
customer = Customer()


while True:
    print("Enter 1 to display avaible books")
    print("Enter 2 to request avaible book")
    print("Enter 3 to retur a book")
    print("Enter 4 to exit")
    userChoice= int(input())

    if userChoice == 1:
        library.displaybooks()

    elif userChoice == 2:
        requestedBook = customer.requestabook()
        library.lendabook(requestedBook)

    elif userChoice == 3:
        returnedBook = customer.returnabook()
        library.addabook(returnedBook)

    elif userChoice == 4:
        quit()


with open("../Daten/books.txt", "r") as file:
    books = file.readlines()
    for book in books:
        book.strip("\n")
        print(book[0] + str(len(book)-1))

#print(books)
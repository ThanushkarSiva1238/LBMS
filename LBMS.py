import datetime as dt

# Lists =================================
Books = []
LendList = []
ReturnList = []
Header = ["ISBN No", "Book Name", "Author", "Published Year", "Quantity"]

Divider = "+" + "-"*7 + "+" + "-"*16 + "+" + "-"*21 + "+" + "-"*21 + "+" + "-"*16 + "+" + "-"*10 + "+"

# Classes ===============================
class LBMS:
    def __init__(self, ISBN_No, Book_Name, Author, Published_Year, Qty):
        self.ISBN_No = ISBN_No
        self.Book_Name = Book_Name
        self.Author = Author
        self.Published_Year = Published_Year
        self.Qty = Qty

class LendBook:
    def __init__(self, Person, Book_Name, count, date, Contact_No):
        self.Person = Person
        self.Book_Name = Book_Name
        self.count = count
        self.date = date
        self.Contact_No = Contact_No

class RtnBook:
    def __init__(self, Person, Book_Name, count, ldate, rdate, Contact_No, Status):
        self.Person = Person
        self.Book_Name = Book_Name
        self.count = count
        self.ldate = ldate
        self.rdate = rdate
        self.Contact_No = Contact_No
        self.Status = Status


# Functions ==============================
def Register():
    print("===== Register Book =====")

    ISBN_No = input("ISBN No : ")
    Book_Name = input("Book Name : ").title()
    Author = input("Author : ").title()
    Published_Year = int(input("Year : "))
    Qty = int(input("Quantity : "))

    Add = LBMS(ISBN_No, Book_Name, Author, Published_Year, Qty)
    Books.append(Add)
    print()

def BookList():
    print("===== Book List =====")

    print(Divider)
    print("| Index".ljust(6), end=" | ")
    print(Header[0].ljust(15), end="| ")
    print(Header[1].ljust(20), end="| ")
    print(Header[2].ljust(20), end="| ")
    print(Header[3].ljust(15), end="| ")
    print(Header[4].ljust(7), end=" |")
    print()
    print(Divider)

    i = 0
    for column in Books:
        i += 1
        a = "| " + str(i)
        print(a.ljust(8), end="| ")
        print(column.ISBN_No.ljust(15), end="| ")
        print(column.Book_Name.ljust(20), end="| ")
        print(column.Author.ljust(20), end="| ")
        print(str(column.Published_Year).ljust(15), end="| ")
        print(str(column.Qty).ljust(8), end=" |")
        print()
    print(Divider)
    print()

def Search():
    print("===== Searching Book =====")

    state = True
    while state:
        print("1. Search through Author Name \n2. Search through Book Name \n3. Go to Back")
        choose1 = int(input("Choose One [1|2|3] : "))
        print()

        if choose1 == 1:
            A = input("Author Name : ").title()
            print()
            print(Divider)
            print("| Index".ljust(6), end=" | ")
            print(Header[0].ljust(15), end="| ")
            print(Header[1].ljust(20), end="| ")
            print(Header[2].ljust(20), end="| ")
            print(Header[3].ljust(15), end="| ")
            print(Header[4].ljust(7), end=" |")
            print()
            print(Divider)

            i = 0
            for search in Books:
                if search.Author == A:
                    i += 1
                    a = "| " + str(i)
                    print(a.ljust(8), end="| ")
                    print(search.ISBN_No.ljust(15), end="| ")
                    print(search.Book_Name.ljust(20), end="| ")
                    print(search.Author.ljust(20), end="| ")
                    print(str(search.Published_Year).ljust(15), end="| ")
                    print(str(search.Qty).ljust(8), end=" |")
                    print()
            print(Divider)

        if choose1 == 2:
            A = input("Book Name : ").title()
            print()
            print(Divider)
            print("| Index".ljust(6), end=" | ")
            print(Header[0].ljust(15), end="| ")
            print(Header[1].ljust(20), end="| ")
            print(Header[2].ljust(20), end="| ")
            print(Header[3].ljust(15), end="| ")
            print(Header[4].ljust(7), end=" |")
            print()
            print(Divider)

            i = 0
            for search in Books:
                if search.Book_Name == A:
                    i += 1
                    a = "| " + str(i)
                    print(a.ljust(8), end="| ")
                    print(search.ISBN_No.ljust(15), end="| ")
                    print(search.Book_Name.ljust(20), end="| ")
                    print(search.Author.ljust(20), end="| ")
                    print(str(search.Published_Year).ljust(15), end="| ")
                    print(str(search.Qty).ljust(8), end=" |")
                    print()
            print(Divider)

        if choose1 == 3:
            state = False

def Lend():
    state = True
    while state:
        print("1. Insert Book Lending Details \n2. Lend Book List \n3. Go to Back")
        choose2 = int(input("Choose One [1|2|3] : "))
        print()

        if choose2 == 1:
            Person = input("Consumer : ").title()
            Contact_No = input("Contact No : ")
            Book_Name = input("Book Name : ").title()
            for row in Books:
                if row.Book_Name == Book_Name:
                    count = int(input("No. of Books : "))
                    date = dt.date.today()
                    row.Qty -= count

            Add = LendBook(Person, Book_Name, count, date, Contact_No)
            LendList.append(Add)

        elif choose2 == 2:
            print("===== Lend Book List =====")
            
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+")
            print("| Index".ljust(6), end=" | ")
            print("Book Name".ljust(20), end="| ")
            print("No. of Books".ljust(13), end="|| ")
            print("Date".ljust(11), end="| ")
            print("Consumer".ljust(21), end="| ")
            print("Contact No".ljust(13), end=" |")
            print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+")

            i = 0
            for ll in LendList:
                i += 1
                a = "| " + str(i)
                print(a.ljust(8), end="| ")
                print(ll.Book_Name.ljust(20), end="| ")
                print(str(ll.count).ljust(13), end="|| ")
                print(str(ll.date).ljust(11), end="| ")
                print(ll.Person.ljust(21), end="| ")
                print(ll.Contact_No.ljust(13), end=" |")
                print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+\n")

        if choose2 == 3:
            state = False

def ReturnBook():
    state = True
    while state:
        print("1. Return Book Details \n2. Return Book List \n3. Go to Back")
        choose3 = int(input("Choose One [1|2|3] : "))
        print()

        if choose3 == 1:
            Person = input("Consumer : ").title()

            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*16 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+")
            print("| Index".ljust(6), end=" | ")
            print("Book Name".ljust(20), end="| ")
            print("No. of Books".ljust(13), end="|| ")
            print("Return Date".ljust(15), end="| ")
            print("Consumer".ljust(21), end="| ")
            print("Contact No".ljust(13), end=" |")
            print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+")
            
            i = 0
            for ll in LendList:
                if ll.Person == Person:
                    i += 1
                    a = "| " + str(i)
                    print(a.ljust(8), end="| ")
                    print(ll.Book_Name.ljust(20), end="| ")
                    print(str(ll.count).ljust(13), end="|| ")
                    print(str(ll.date).ljust(15), end="| ")
                    print(ll.Person.ljust(21), end="| ")
                    print(ll.Contact_No.ljust(13), end=" |")
                    print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*12 + "+" + "-"*22 + "+" + "-"*15 + "+\n")

            Book_Name = input("Book Name : ").title()
            Status = input("Status [ Good | Damaged ] : ").title()

            for row in LendList:
                if row.Person == Person and row.Book_Name == Book_Name:
                    date = dt.date.today()
                    Add = RtnBook(Person, Book_Name, ll.count, ll.date, date, ll.Contact_No, Status)
                    ReturnList.append(Add)

                    for col in Books:
                        if col.Book_Name == Book_Name:
                            col.Qty += row.count

                    LendList.remove(row)

        elif choose3 == 2:
            print("===== Return Book List =====")
            
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*13 + "+" + "-"*13 + "+" + "-"*19 + "+" + "-"*15 + "++" + "-"*9 + "+")
            print("| Index".ljust(6), end=" | ")
            print("Book Name".ljust(20), end="| ")
            print("No. of Books".ljust(13), end="|| ")
            print("Lend Date".ljust(12), end="| ")
            print("Return Date".ljust(12), end="| ")
            print("Consumer".ljust(18), end="| ")
            print("Contact No".ljust(13), end=" || ")
            print("Status".ljust(8), end="|")
            print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*13 + "+" + "-"*13 + "+" + "-"*19 + "+" + "-"*15 + "++" + "-"*9 + "+")

            i = 0
            for RL in ReturnList:
                i += 1
                a = "| " + str(i)
                print(a.ljust(8), end="| ")
                print(RL.Book_Name.ljust(20), end="| ")
                print(str(RL.count).ljust(13), end="|| ")
                print(str(RL.ldate).ljust(12), end="| ")
                print(str(RL.rdate).ljust(12), end="| ")
                print(RL.Person.ljust(18), end="| ")
                print(RL.Contact_No.ljust(13), end=" || ")
                print(RL.Status.ljust(8), end="|")
                print()
            print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*14 + "++" + "-"*13 + "+" + "-"*13 + "+" + "-"*19 + "+" + "-"*15 + "++" + "-"*9 + "+\n")

        if choose3 == 3:
            state = False


# Sample Data
li = [["2403840", "Avengers", "Stan Lee", 2003, 10], ["0840384", "Justice League", "Steve", 2000, 10], ["8058380", "Spider Man", "Stan Lee", 1990, 20], ["84058353", "Harry Potter", "UnKnown", 1999, 10]]
for i in li:
    Books.append(LBMS(i[0], i[1], i[2], i[3], i[4]))
    

# Main Content ============================
print("Library Management System - ABC PVT")
value = True

while value:
    print("1. Register \n2. Book List \n3. Search \n4. Lends \n5. Return Books \n6. Exit")
    choose = int(input("Choose One [1|2|3|4|5|6] : "))

    match(choose):
        case 1:
            Register()

        case 2:
            BookList()

        case 3:
            Search()

        case 4:
            Lend()

        case 5:
            ReturnBook()

        case 6:
            value = False

        case _:
            print("Please, choose correct one...")

    
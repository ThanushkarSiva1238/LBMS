import datetime as dt

# Lists =================================
Books = []
LendList = []
ReturnList = []
Header = ["ISBN No", "Book Name", "Author", "Published Year", "Quantity"]


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
def BList(l):
    print("+" + "-"*7 + "+" + "-"*16 + "+" + "-"*21 + "+" + "-"*21 + "+" + "-"*16 + "+" + "-"*10 + "+")
    print("| Index".ljust(6), end=" | ")
    print(Header[0].ljust(15), end="| ")
    print(Header[1].ljust(20), end="| ")
    print(Header[2].ljust(20), end="| ")
    print(Header[3].ljust(15), end="| ")
    print(Header[4].ljust(7), end=" |")
    print()
    print("+" + "-"*7 + "+" + "-"*16 + "+" + "-"*21 + "+" + "-"*21 + "+" + "-"*16 + "+" + "-"*10 + "+")

    i = 0
    for column in l:
        i += 1
        a = "| " + str(i)
        print(a.ljust(8), end="| ")
        print(column.ISBN_No.ljust(15), end="| ")
        print(column.Book_Name.ljust(20), end="| ")
        print(column.Author.ljust(20), end="| ")
        print(str(column.Published_Year).ljust(15), end="| ")
        print(str(column.Qty).ljust(8), end=" |")
        print()
    print("+" + "-"*7 + "+" + "-"*16 + "+" + "-"*21 + "+" + "-"*21 + "+" + "-"*16 + "+" + "-"*10 + "+")

def LList(l):
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 12 + "+" + "-" * 22 + "+" + "-" * 15 + "+")
    print("| Index".ljust(6), end=" | ")
    print("Book Name".ljust(20), end="| ")
    print("No. of Books".ljust(13), end="|| ")
    print("Date".ljust(11), end="| ")
    print("Consumer".ljust(21), end="| ")
    print("Contact No".ljust(13), end=" |")
    print()
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 12 + "+" + "-" * 22 + "+" + "-" * 15 + "+")

    i = 0
    for ll in l:
        i += 1
        a = "| " + str(i)
        print(a.ljust(8), end="| ")
        print(ll.Book_Name.ljust(20), end="| ")
        print(str(ll.count).ljust(13), end="|| ")
        print(str(ll.date).ljust(11), end="| ")
        print(ll.Person.ljust(21), end="| ")
        print(ll.Contact_No.ljust(13), end=" |")
        print()
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 12 + "+" + "-" * 22 + "+" + "-" * 15 + "+")

def RList(l):
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 19 + "+" + "-" * 15 + "++" + "-" * 9 + "+")
    print("| Index".ljust(6), end=" | ")
    print("Book Name".ljust(20), end="| ")
    print("No. of Books".ljust(13), end="|| ")
    print("Lend Date".ljust(12), end="| ")
    print("Return Date".ljust(12), end="| ")
    print("Consumer".ljust(18), end="| ")
    print("Contact No".ljust(13), end=" || ")
    print("Status".ljust(8), end="|")
    print()
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 19 + "+" + "-" * 15 + "++" + "-" * 9 + "+")

    i = 0
    for RL in l:
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
    print("+" + "-" * 7 + "+" + "-" * 21 + "+" + "-" * 14 + "++" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 19 + "+" + "-" * 15 + "++" + "-" * 9 + "+\n")

def SortAlgorithm(OGList, a):
    list = []
    reorder = []

    def Algo(list, z, reorder):
        print("Choose Sorting Algorithms : \n\t1. Bubble Sort \n\t2. Selection Sort \n\t3. Insertion Sort \n\t4. Exit")
        choose5 = int(input("Choose One [1|2|3] : "))
        l = len(list)

        if choose5 == 1:
            print("1. Ascending Order \n2. Descending Order")
            order = int(input("Select One : "))
            print("++++++ Bubble Sort ++++++")

            if order == 1:
                for i in range(l):
                    for j in range(0, l - 1):
                        if list[j] > list[j + 1]:
                            temp = list[j]
                            list[j] = list[j + 1]
                            list[j + 1] = temp

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

            elif order == 2:
                for i in range(l):
                    for j in range(0, l - 1):
                        if list[j] < list[j + 1]:
                            temp = list[j]
                            list[j] = list[j + 1]
                            list[j + 1] = temp

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

        elif choose5 == 2:
            print("1. Ascending Order \n2. Descending Order")
            order = int(input("Select One : "))
            print("++++++ Selection Sort ++++++")

            if order == 1:
                for i in range(l):
                    min = i
                    for j in range(min + 1, l):
                        if (list[j] < list[min]):
                            min = j
                    (list[i], list[min]) = (list[min], list[i])

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

            elif order == 2:
                for i in range(l):
                    min = i
                    for j in range(min + 1, l):
                        if (list[j] > list[min]):
                            min = j
                    (list[i], list[min]) = (list[min], list[i])

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

        elif choose5 == 3:
            print("1. Ascending Order \n2. Descending Order")
            order = int(input("Select One : "))
            print("++++++ Insertion Sort ++++++")

            if order == 1:
                for i in range(1, l):
                    a = list[i]
                    j = i-1

                    while j <= 0 and a > list[j]:
                        list[j+1] = list[j]
                        j -= 1

                    list[j+1] = a

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

            elif order == 2:
                for i in range(l):
                    min = i
                    for j in range(min + 1, l):
                        if (list[j] > list[min]):
                            min = j
                    (list[i], list[min]) = (list[min], list[i])

                for id in list:
                    for column in OGList:
                        if id == getattr(column, z):
                            reorder.append(column)

    if a == "BookList":
        print("1. Sort via ISBN No \n2. Sort via Book Name \n3. Exit")
        s = int(input("Select One [1|2|3] : "))

        if s == 1:
            for i in OGList:
                z = "ISBN_No"
                list.append(i.ISBN_No)
            Algo(list, z, reorder)
            BList(reorder)
            print()

        elif s == 2:
            for i in OGList:
                z = "Book_Name"
                list.append(i.Book_Name)
            Algo(list, z, reorder)
            BList(reorder)
            print()

        else:
            print()
            return

    if a == "LendList":
        print("1. Sort via Book Name \n2. Sort via Date \n3. Exit")
        s = int(input("Select One [1|2|3] : "))

        if s == 1:
            for i in OGList:
                z = "Book_Name"
                list.append(i.Book_Name)
            Algo(list, z, reorder)
            LList(reorder)
            print()

        elif s == 2:
            for i in OGList:
                z = "date"
                list.append(i.date)
            Algo(list, z, reorder)
            LList(reorder)
            print()

        else:
            print()
            return

    if a == "ReturnList":
        print("1. Sort via Book Name \n2. Sort via Lend Date \n3. Sort via Return Date \n4. Exit")
        s = int(input("Select One [1|2|3|4] : "))

        if s == 1:
            for i in OGList:
                z = "Book_Name"
                list.append(i.Book_Name)
            Algo(list, z, reorder)
            RList(reorder)
            print()

        elif s == 2:
            for i in OGList:
                z = "ldate"
                list.append(i.ldate)
            Algo(list, z, reorder)
            RList(reorder)
            print()

        elif s == 3:
            for i in OGList:
                z = "rdate"
                list.append(i.rdate)
            Algo(list, z, reorder)
            RList(reorder)
            print()

        else:
            print()
            return


# Main Functions =========================
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

    BList(Books)
    print()

    sel = "BookList"
    SortAlgorithm(Books, sel)

def Search():
    print("===== Searching Book =====")

    state = True
    while state:
        reorder = []
        print("1. Search through Author Name \n2. Search through Book Name \n3. Go to Back")
        choose1 = int(input("Choose One [1|2|3] : "))
        print()

        if choose1 == 1:
            A = input("Author Name : ").title()

            for search in Books:
                if search.Author == A:
                    reorder.append(search)
            BList(reorder)
            print()

        if choose1 == 2:
            A = input("Book Name : ").title()

            for search in Books:
                if search.Book_Name == A:
                    reorder.append(search)
            BList(reorder)
            print()

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
            LList(LendList)
            print()

            sel = "LendList"
            SortAlgorithm(LendList, sel)


        if choose2 == 3:
            state = False

def ReturnBook():
    state = True
    while state:
        print("1. Return Book Details \n2. Return Book List \n3. Go to Back")
        choose3 = int(input("Choose One [1|2|3] : "))
        print()

        if choose3 == 1:
            reorder = []
            Person = input("Consumer : ").title()

            for ll in LendList:
                if ll.Person == Person:
                    reorder.append(ll)
            LList(reorder)


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

            RList(ReturnList)
            print()

            sel = "ReturnList"
            SortAlgorithm(ReturnList, sel)

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

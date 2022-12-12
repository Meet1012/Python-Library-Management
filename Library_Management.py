import time


class library:
    Librarians = [["Meet", "1234"]]       #storing the data
    Students = [["Meet", "0000"]]
    Rack_Book = [["Physics", "Einstin", "1000"], ["Physics", "Einstin", "1001"], ["Physics", "Edison", "1002"], ["Physics", "Einstin", "1003"], ["Physics", "Einstin", "1004"],
                 ["Chemistry", "Einstin", "2000"], ["Chemistry", "Thamos", "2001"], ["Chemistry", "Einstin", "2002"], ["Chemistry", "Nobel", "2003"], ["Chemistry", "Einstin", "2004"]]
    Dispatch_Book = []


# change login information
def Change_Login():
    if [name, pin] not in lib.Librarians:
        library.Librarians.append([name, pin])
        print("Changing Login details.......")
        time.sleep(1)
        print("Successfully Changed login details")
    else:
        print("Entered same details only")


# update status of Book
def Update_Book():
    if [name, author, Bid] not in lib.Rack_Book:

        library.Rack_Book.append([name, author, Bid])

        print("Updating Book in Library.......  ")
        time.sleep(1)
        print("Update Successfully:", [name, author, Bid])
    else:
        print("Book already available with same details")


# to get the detail about the book
def Details_Books():
    print("--------------------------------------------------")
    print("Book name", " "*9, "Author Name", " "*9, "Book ID")
    print("--------------------------------------------------")

    for i in range(len(library.Rack_Book)):
        print(library.Rack_Book[i][0], " "*13,
              library.Rack_Book[i][1], " "*13, lib.Rack_Book[i][2])
        print("--------------------------------------------------")

    print("\nNo of avaliable Books are:", len(lib.Rack_Book))


# for adding the students    
def Add_Students():
    if [name, pin] not in lib.Students:
        library.Students.append([name, pin])
        print("Adding student Details.......")
        time.sleep(1)
        print("Successfully Added with details", [name, pin])
    else:
        print("Students already available with details")


# for deleting students
def Delete_Students(name, pin):
    if [name, pin] in lib.Students:
        library.Students.remove([name, pin])
        print("Deleting Student Details........")
        time.sleep(1)
        print("Successfully deleted details", [name, pin])
    else:
        print("No students available with details")


# inquiry of students
def Details_Students():
    print("-------------------------------")
    print("Sudent name", " "*9, "R.No")
    print("-------------------------------")

    for i in range(len(lib.Students)):
        print(library.Students[i][0], " "*15, lib.Students[i][1])
        print("-------------------------------")
    print("\nNo of Students are:", len(library.Students))

# issue the book
def Collect_Books():
    if [name, author, Bid] in lib.Rack_Book:
        library.Dispatch_Book.append([name, author, Bid])
        library.Rack_Book.remove([name, author, Bid])
        print("Book collected succesfully:", [
              name.capitalize(), author.capitalize(), Bid])
    else:
        print("Enter details wrong:")


# return the book
def Return_Book():
    if [name, author, Bid] in library.Dispatch_Book:
        library.Dispatch_Book.remove([name, author, Bid])
        library.Rack_Book.append([name, author, Bid])
        print("Returned Successfully:", [
              name.capitalize(), author.capitalize(), Bid])
    else:
        print("Enter details wrong:")


lib = library
print("Welcome to Library")
while(True):
    print('''Select your Option
     1:Librarian Login
     2:Student Login
     3:Exit''')

    opt1 = int(input("Please Enter your option:"))

    if opt1 == 1:
        i = 1
        while (i < 4):
            usrlib = input("Please Enter your Name:")
            pinlib = input("Please Enter your Login PIN:")
            if [usrlib, pinlib] in library.Librarians:
                print("Verifying.....")
                time.sleep(1)
                print("Access Granted")
                i = 5
                while(True):
                    print('''Select your Option
                     0:Change Username or Password   
                     1:Add Books
                     2:Books Details
                     3:Add Students
                     4:Remove Students
                     5:Students details
                     6:Exit or Back''')
                    opt2 = int(input("Please Enter your option:"))
                    if opt2 == 0:
                        usrlib1 = input("Please Enter User Name to change:")
                        pinlib2 = input("Please Enter Login PIN to change:")
                        Change_Login(usrlib1, pinlib2)

                    elif opt2 == 1:
                        name = input("Please Enter your Book Name:")
                        author = input("Please Enter your Book Author:")
                        Bid = input("Please Enter your Book Id:")
                        Update_Book(name.capitalize(),
                                    author.capitalize(), Bid)

                    elif opt2 == 2:
                        Details_Books()

                    elif opt2 == 3:
                        name = input("Please Enter Student Name:")
                        pin = input("Please Enter Student R.No:")
                        Add_Students(name.capitalize(), pin)
                    elif opt2 == 4:
                        name = input("Please Enter Student Name:")
                        pin = input("Please Enter Student R.No:")
                        Delete_Students(name.capitalize(), pin)
                    elif opt2 == 5:
                        Details_Students()

                    elif opt2 == 6:
                        print("Back to Menu")
                        break
                    else:
                        print("Wrong input")
                        continue
            elif [usrlib, pinlib]not in library.Librarians:
                print("\nAccess Denied \nUser name or PIN Entered wrong")
                print("\nYou have more", (3-i), "attempts")
                i += 1
                if i == 4:
                    print("Failed login within 3 attempts")
                    print("Retry!!!\n")
                    break

    elif opt1 == 2:
        i = 4
        while (i >= 1):
            usrstd = input("Please Enter your Name: ")
            pinstd = input("Please Enter your R.No: ")

            if [usrstd, pinstd] in lib.Students:
                print("Access Granted")
                while(True):
                    print('''Select your Option
                         1:Collect Book
                         2:Return Books
                         3:Exit or Back
                         ''')
                    opt2 = int(input("Please Enter your option:"))
                    if opt2 == 1:
                        print("Availablie Books are:\n")
                        Details_Books()
                        name = input("Please Enter your Book Name:")
                        author = input("Please Enter your Book Author:")
                        Bid = input("Please Enter your Book Id:")
                        Collect_Books()
                    elif opt2 == 2:
                        name = input("Please Enter your Book Name:")
                        author = input("Please Enter your Book Author:")
                        Bid = input("Please Enter your Book Id:")
                        Return_Book()
                    elif opt2 == 3:
                        print("Back to Menu")
                        break
            elif i == 1:
                print("Out of Chances.\n")
                break
            
            else:
                print("\nOnly ", i-1, "chances Left.\n")
                i = i-1

    elif opt1 == 3:
        print("Shutting Down......")
        time.sleep(1)

        break
    else:
        print("Wrong input")
        

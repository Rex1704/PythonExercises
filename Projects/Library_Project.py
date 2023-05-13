class Library:
    def __init__(self,listOfBooks,libraryName):
        self.books = listOfBooks
        self.name = libraryName
        self.lendInfo = dict()

    def displaybooks(self):
        for i in self.books:
            print(i)

    def book_lend(self,lendername,book):
        for i in self.books:
            if(book==i):
                self.lendInfo[book]=lendername
                self.books.remove(i)
                break
            else:
                for key,value in self.lendInfo.items():
                    if (key==book):
                        print(f"{key} is lended by {value}")
                        break
                else:
                    print(f"{book} is not available in our library")



    def book_return(self,returnername,book):
        if(self.lendInfo[book]==returnername):
            self.lendInfo.pop(book)
            self.books.append(book)
        else:
            print("Please check your given info again!! ")

    def add_book(self,bookname):
        if type(bookname)=="<class 'list'>":
            for i in bookname:
                self.books.append(i)
        else:
            self.books.append(bookname)


if __name__ == '__main__':
    print("\t\t\t******Welcome To Library******")
    libraries = list()
    selected_Library = None
    while(True):
        first=int(input("1.CreateLibrary\n2.UseLibrary\n0.ToExit"))
        if(first==1):
            library_Name = input("Enter Name of your library: ")
            library_Books = input("Enter books name seperated by one space: ").split(" ")
            print("Creating library......")
            libraries.append((Library(library_Books,library_Name)))
            print("Library Created!")
        elif(first==2):
            if(len(libraries)>1):
                for count,library in enumerate(libraries):
                    print(f"{count+1}. {library.name}")
                select_Library = int(input("To Select a library enter their associated no. :"))
                selected_Library = libraries[select_Library - 1]
            elif(len(libraries)==1):
                selected_Library = libraries[0]
            else:
                print("There is no library present at current time")
                break
            use = int(input("1.LendBook\n2.ReturnBook\n3.AddBook"))
            if(use==1):
                lendername = input("Enter your name:")
                bookname = input("Enter book name:")
                selected_Library.book_lend(lendername,bookname)
            elif(use==2):
                returnername = input("Enter your name:")
                bookname = input("Enter book name:")
                selected_Library.book_return(returnername,bookname)
            elif(use==3):
                tobeaddedbook = input("Enter the book which you want to add in this library:")
                selected_Library.add_book(tobeaddedbook)
            elif(use==0):
                break

        elif(first==0):
            break

#Library Management System 
class Publication:   # creates a class called Publication
    def __init__(self, title, author): #creates a constructor method that initializes the title and author attributes of the Publication class
        self.title = title
        self.author = author
    
    def get_title(self): # creates a method that returns the title attribute of the Publication class
        return self.title

    def get_author(self): # creates a method that returns the author attribute of the Publication class
        return self.author

    def set_title(self, title): # creates a method that sets the title attribute of the Publication class
        self.title = title

    def set_author(self, author): # creates a method that sets the author attribute of the Publication class
        self.author = author    

    def display_info(self): # displays the title and author attributes of the Publication class
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Publication): # creates a class called Book that inherits from Publication
    def __init__(self, title, author, number_of_pages): # creates a constructor method that initializes the title, author, and number_of_pages attributes of the Book class
        super().__init__(title, author) # super is used to call the constructor of the parent class (Publication) to initialize the title and author attributes
        self.number_of_pages = number_of_pages

    def get_number_of_pages(self): # creates a method that returns the number_of_pages attribute of the Book class
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages
        if number_of_pages <= 0:  # checks if the issue number is less than or equal to 0, and if it is it prints an error message
            print("Number of pages must be a positive integer.")

    def display_info(self):
        super().display_info() # super is used to call the display_info method of the parent class (Publication) to display the title and author attributes
        print(f"Number of Pages: {self.number_of_pages}")


class Magazine(Publication):# creates a class called Magazine that inherits from Publication


    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # super is used to call the constructor of the parent class (Publication) to initialize the title and author attributes
        self.issue_number = issue_number 

    def get_issue_number(self): # creates a method that returns the issue_number attribute of the Magazine object
        return self.issue_number

    def set_issue_number(self, issue_number): # creates a method that sets the issue_number attribute of the Magazine class
        self.issue_number = issue_number
        if issue_number <= 0: # checks if the issue number is less than or equal to 0, and if it is it prints an error message
            print("Issue number must be a positive integer.")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

#Objects

#Creating publication object
pub1 = Publication("The Great Gatsby", "F. Scott Fitzgerald")
pub2 = Publication("To Kill a Mockingbird", "Harper Lee")

#Creating book object
book1 = Book("Hunger Games", "Suzanne Collins", 328)
book2 = Book("1984", "George Orwell", 328)

#Creating magazine object
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time", "Various Authors", 101)

#Printing the information

print("Publication Information:")
pub1.display_info()
pub2.display_info()

print("\nBook Information:")
book1.display_info()
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
mag2.display_info()

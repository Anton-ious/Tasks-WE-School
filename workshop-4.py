class Student:
    school_name="WE-school"
    def __init__(self, name,grade):
        self.name = name
        self.grade = grade
    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")

student1= Student('Ahmed',90)
student1.display_info()
student2= Student('Mohamed',90)
student2.display_info()

##--------------------------------  Q-2 --------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book {self.title} by {self.author} has been borrowed.")
        else:
            print(f"The book {self.title} by {self.author} is already borrowed.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book {self.title} by {self.author} has been returned.")
        else:
            print(f"The book {self.title} by {self.author} is not borrowed.")

book= Book("Python","Ahmed Ali")
book.borrow_book()
book.return_book()
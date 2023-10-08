# A class is a blue-print for creating objects.
# In this code implementation of OOP in Python, 
# we shall implement an object-oriented database for the UG Student MIS


# ---------------------------------------------------------------

# SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name[0]}{first_name[5]}{first_name[1]}{last_name}@st.ug.edu.gh'.lower()

    def full_name(self):
        return  self.first_name + ' ' + self.last_name
    def intials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'   

# creating person object
person = Person("Nana Yaa", "Doku-Amponsah")
# printing the full name
print(person.full_name())
print(person.intials())
print(person.email)

# -------------------------------------------------------------------
        

# SECTION TWO
# 1. Define a class Student which inherites from the Person class
# 2. Define extra attributes for student, such as hall of residence and courses
# 3. Create a student object from the Student class

class Student(Person):
    def __init__(self, first_name, last_name, hall_of_residence, courses = None):
        super().__init__(first_name, last_name)
        self.hall_of_residence = hall_of_residence
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        # self.courses = courses
    
    def add_course(self, course_title):
        if course_title not in self.courses:
            self.courses.append(course_title)
    def drop_course(self, course_title):
        if course_title in self.courses:
            self.courses.remove(course_title)
    def print_all_courses(self):
        print(f'{self.full_name()} has registered {len(self.courses)} courses.')
        print('-'*50)
        for courses in self.courses:            
            print(courses)

student = Student("Nana Yaa", "Doku-Amponsah", "Dr.Hilla Limann Hall")
print(student.hall_of_residence)

student.add_course('Python')
student.add_course('Calculus')
student.add_course('Calculus')
student.add_course('African Studies')
student.add_course('Project Work')

# student.drop_course("Calculus")
# student.drop_course('Python')

# print(student.courses)
student.print_all_courses()



# -----------------------------------------------------------------------------------


# """
# 4. Write a add_course, drop_course, print_all_courses method to mimic 
# a real-world use-case of activities of adding a course, 
# deleting a course and printing registered courses respectively
# a student will perform on the Student MIS 

# """

# Magic Methods
# Overwrite string method

































































































































































































































































# class Student:
#     def __init__(self):
#         self.courses = []

#     def add_course(self, course):
#         if course not in self.courses:
#             self.courses.append(course)
#             print(f"Added {course}")
#         else:
#             print(f"{course} is already in your courses")

#     def drop_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#             print(f"Dropped {course}")
#         else:
#             print(f"{course} is not in your courses")

#     def print_all_courses(self):
#         if self.courses:
#             print("Your courses:")
#             for course in self.courses:
#                 print(course)
#         else:
#             print("You are not registered in any courses")

# # Example usage:
# student = Student()
# student.add_course("Math")
# student.add_course("Science")
# student.print_all_courses()  # Your courses: Math\nScience
# student.drop_course("Math")
# student.print_all_courses()  # Your courses: Science
# student.drop_course("Math")  # Math is not in your courses

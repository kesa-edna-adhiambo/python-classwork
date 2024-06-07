class Student:
    school = 'Akirachix'
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code


    def greet_student(self):
         greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}"
         return greeting


    def greet_with_year(self):
        greeting = f"Hello {self.first_name}, you were born in {2024 - self.age}"
        return greeting


    # python program to print initials of a name
    # def student_initials(self):
    #     first_name = self.lower

 



    def  student_full_name(self):
        my_names = f" Hello {self.first_name} {self.last_name}"
        return my_names

    def student_enroll(self):
        enrollment = f"Hello {self.first_name} {self.last_name}, you have been enrolled to {self.school}"
        return enroll







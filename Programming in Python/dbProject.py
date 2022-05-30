class Student:
    #Defines the student class for the 'database'.  Database is essentially a list of Student objects.
    #'class' property is renamed to section here to avoid conflict with Python
    def __init__(self, name, address, section, *grades):
        self.name = name
        self.address = address
        self.section = section
        self.maths = grades[0]
        self.



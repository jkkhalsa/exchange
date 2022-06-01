#Python Database Project
#Benedetta Felici, Luca whatshisface, and James Khalsa
#Turned in <DATE>



class Student:
    #Defines the student class for the 'database'.  Database is essentially a list of Student objects.
    #'class' property is renamed to 'section' here to avoid conflict with Python
    def __init__(self, name, address, section, *grades):
        self.name = name
        self.address = address
        self.section = section
        self.grades = grades

        print("For testing, grades are", grades)

    #returns csv line to be written to text file
    def write(self):
        toWrite = self.name + "," + self.address + "," + self.section
        for grade in self.grades:
            toWrite += ","
            toWrite += str(grade)
        toWrite += "\n"
        return toWrite

    def editName(self, newName):
        self.name = newName

    def editAddress(self, newAddress):
        self.address = self.newAddress

    def editClass(self, newSection):
        self.section = newSection

    def editGrade(self, newGrade, classEdited):
        #0 - math, 1 - science, 2 - english, 3 - dutch, 4 - arts
        self.grades[classEdited] = newGrade



class StudentList:
    def __init__(self, filePath):
        self.students = []
        self.sorted = False
        with open(filePath) as input:
            for index, line in enumerate(input):
                line = line.replace('\n', '')
                if line: ##make sure this isn't an empty line
                    temp = line.split(",")
                    #check if we have the correct amount of information/formatting is correct
                    if len(temp) == 8:
                        #cast grades to numbers
                        for i in range(3, 8):
                            temp[i] = float(temp[i])
                        #create a new student object
                        newStudent = Student(temp[0], temp[1], temp[2], [temp[i] for i in range(3, 8)])
                        #add the new student to our own internal records
                        self.addStudent(newStudent)
                    else:
                        print("Error on line", index, ".  Check information.")


    def addStudent(self, student):
        self.students.append(student)
        self.sorted = False

    def search(self, studentName):
        #insert search function
        #return index of student and student's data
        #faster to search if it's sorted by name, that's what sorted flag is for
        pass

    def delete(self, index):
        #insert deletion by index
        #return data of student deleted
        pass

    def edit(self, index):
        #insert editing by index
        pass

    def sort(self, type):
        #insert sort by grades or alphabetically
        #merge sort?
        #OPTIONAL.
        #if sorted by name, put sort flag to TRUE
        pass

    def save(self, filepath):
        writing = open(filepath, 'w')
        for student in self.students:
            writing.write(student.write())
        writing.close()




list = StudentList("newtext.txt")

        



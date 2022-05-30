#Python Project
#Benedetta Felici and James Khalsa
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

    #allows student object to be written to the text file in comma separated format
    def write(self, filePath):
        writing = open(filePath, "a")
        toWrite = self.name + "," + self.address + "," + self.section
        for grade in self.grades:
            toWrite += ","
            toWrite += str(grade)
        toWrite += "\n"
        writing.write(toWrite)
        writing.close()


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



list = StudentList("newtext.txt")

        



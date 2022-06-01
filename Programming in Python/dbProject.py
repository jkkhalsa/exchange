#Python Database Project
#Benedetta Felici, Luca whatshisface, and James Khalsa
#Turned in <DATE>


from os import access, W_OK, R_OK
from os.path import isfile


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
        self.address = newAddress

    def editClass(self, newSection):
        self.section = newSection

    def editGrade(self, newGrade, classEdited):
        #0 - math, 1 - science, 2 - english, 3 - dutch, 4 - arts
        self.grades[classEdited] = newGrade



class StudentList:
    def __init__(self, filePath):
        self.students = []
        self.sorted = False
        print(filePath)
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
        self.students.remove(index)

    def edit(self, index, newInfo, toEdit):
        #insert editing by index

        self.students[index].editName(newInfo)

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




runFlag = True
print("Welcome.  Please give us the database file (.txt extension included):")
filePath = input()
filePath = filePath.replace('\n', '')
list = StudentList(filePath)

while(runFlag):  
    print("\nPlease select what you'd like to do.")
    print("Options:\n1\tAdd new record\n2\tDelete a record\n3\tEdit a record\n4\tSearch students by name\n5\tSave and exit\n6\tExit without saving")
    choice = input()
    match choice:
        case 1:
            print("Please give us the name, address, class, and grades of the student, separated by commas.")
            newInfo = input()
            newInfo = newInfo.replace(' ', '')
            newInfo  = newInfo.split(',')
            if (len(newInfo) == 8):
                newStudent = Student(newInfo)
                list.addStudent(newStudent)
                print("Student", newInfo[0], "added.")
            else:
                print("Error in information given.  Please remember to separate values by commas and enter these values only: name, address, class, math grade, science grade, English grade, Dutch grade, and art grade.")

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass
        
        case 5:
            pass

        case 6:
            pass

        case _:
            print("Invalid choice.  Reprinting options.")  
    
    


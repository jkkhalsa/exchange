#Python Database Project
#Benedetta Felici, Luca whatshisface, and James Khalsa
#Turned in <DATE>


class Student:
    #Defines the student class for the 'database'.  Database is essentially a list of Student objects.
    #'class' property is renamed to 'section' here to avoid conflict with Python
    def __init__(self, name, address, section, grades):
        self.name = name
        self.address = address
        self.section = section
        self.grades = grades

    #returns csv line to be written to text file
    def write(self):
        toWrite = self.name + "," + self.address + "," + self.section
        for grade in self.grades:
            toWrite += ","
            toWrite += str(grade)
        toWrite += "\n"
        return toWrite


        #SETTER methods - write properties of student
    def editName(self, newName):
        self.name = newName

    def editAddress(self, newAddress):
        self.address = newAddress

    def editClass(self, newSection):
        self.section = newSection

    def editGrade(self, newGrade, classEdited):
        #0 - math, 1 - science, 2 - english, 3 - dutch, 4 - arts
        self.grades[classEdited] = newGrade


        #GETTER methods - read properties of student
    def getName(self):
        return self.name
    
    def getGrades(self, index):
        return self.grades[index]



class StudentList:
        #WORKING AND FINISHED
    def __init__(self, filePath):
        self.students = []
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
        return


        #add student to list
    def addStudent(self, student):
        self.students.append(student)
        return

        #search for a student by name
        #returns index of student, student information
    def search(self, studentName, isLast):
        namelist = []
        #make a list of names, first and last - 2D array
        for each in self.students:
            namelist.append(each.getName().split())
        #go through the list of names and find the one we want
        #use isLast to know which half of the 2d to search
        for index, name in enumerate(namelist):
            if(studentName == name[isLast]): #found name
                return [index, self.students[index].write()]
        return [-1, "none"] #if name not found, tell main menu


        #delete student by index
        #returns name of removed student
    def delete(self, index):
        if (index < len(self.students)):
            removed = self.students.pop(index) #'pop' is better than 'remove' for this because it returns the object removed
            return removed.getName()
        else:
            return "error"

        #edit student information by index
    def edit(self, index, newInfo, toEdit):
        #if we're editing a grade, try to make it a number
        if(toEdit != "name" and toEdit != "address" and toEdit != "section"):
            try:
                newInfo = float(newInfo)
            except: #input error kick back to menu
                print("Error.  Grades must be entered as a number.")
                return
        match toEdit: #edit information based on user input toEdit
            case "name": self.students[index].editName(newInfo)
            case "address": self.students[index].editAddress(newInfo)
            case "section": self.students[index].editClass(newInfo)
            case "math": self.students[index].editGrade(newInfo, 0)
            case "science": self.students[index].editGrade(newInfo, 1)
            case "english": self.students[index].editGrade(newInfo, 2) 
            case "dutch": self.students[index].editGrade(newInfo, 3)
            case "arts": self.students[index].editGrade(newInfo, 4)
            case _: print("Error: Incorrect selection.  Maybe check spelling?")
        return


        #sort students by grades
        #sortBy selects which class' grades will be sorted on
        #0 - math, 1 - science, 2 - english, 3 - dutch, 4 - arts
    def sort(self, sortBy):
        n=len(self.students)
        #simple linear sort, not that efficient but we're working with small data sets
        for i in range (0, n):
            for j in range (i, n):
                if (self.students[i].getGrades(sortBy) < self.students[j].getGrades(sortBy)):
                    aux=self.students[i]
                    self.students[i] = self.students[j]
                    self.students[j] = aux
        return

        #save our working student list to the original file
    def save(self, filepath):
        writing = open(filepath, 'w')
        #write each student to the file
        for student in self.students:
            writing.write(student.write())
        writing.close()
        return




#ACTUAL PROGRAM START.
runFlag = True
print("Welcome.  Please give us the database file (.txt extension included):")
filePath = input()
filePath = filePath.replace('\n', '') #clean up just in case
list = StudentList(filePath) #create our list of students to work with based on this file

#now we loop through the menu until told not to. runFlag will only turn false if user chooses to quit.
while(runFlag):  
    print("\nPlease select what you'd like to do.")
    print("Options:\n1\tAdd new record\n2\tDelete a record\n3\tEdit a record\n4\tSearch students by name\n5\tSort students by grades\n6\tSave and exit\n7\tExit without saving")
    #casting choice to an int, so try/except is needed
    try:
        choice = int(input("Enter selection: "))
    except:
        print("Please make sure you type one of the numbers above.")
    else:
        #based on user input, carry out selected actions
        #each one of these cases requires a bit more information, and then will kick to the StudentList function designed to handle it
        match choice:
            case 1: #add new record
                print("Please give us the name, address, class, and grades of the student, separated by commas.")
                newInfo = input()
                newInfo = newInfo.replace(' ', '')
                newInfo  = newInfo.split(',')
                if (len(newInfo) == 8): #make sure we have the correct amount of information
                    newStudent = Student(newInfo)
                    list.addStudent(newStudent)
                    print("Student", newInfo[0], "added.")
                else:
                    print("Error in information given.  Please remember to separate values by commas and enter these values only: name, address, class, math grade, science grade, English grade, Dutch grade, and art grade.")

            case 2: #delete record
                try:
                    index = int(input("Please give us the index of the student being deleted:\t"))
                except:
                    print("Error.  Please remember the index is to be a whole number.")
                else:
                    deletedName = list.delete(index)
                    if(deletedName != "error"):
                        print("Student", deletedName, "successfully removed.")
                    else:
                        print("Student not removed.  Index out of bounds.")

            case 3: #edit record
                try:
                    index = int(input("Please give us the index of the student being edited:\t"))
                except:
                    print("Error.  Please remember the index is to be a whole number.")
                else:
                    print("Please give us the category to be edited, and the new information.")
                    print("The category may be: Name, Address, Class, Math, Science, English, Dutch, or Arts.")
                    category = input("Category to be edited:\t").lower()
                    newInfo = input("Corrected or new information:\t")
                    list.edit(index, newInfo, category)

            case 4: #search by name
                print("Would you like to search by first or last name?")
                isLast = input("(Type 'first' or 'last'):\t").lower()
                name = input("Name of student to be searched:\t")
                if(isLast == "first"):
                    found = list.search(name, 0)
                elif(isLast == "last"):
                    found = list.search(name, 1)
                else:
                    print("Error.  Please check spelling on 'first' or 'last'.")

                if(found[0] != -1):
                    print("Found at index", found[0], "with information", found[1])
                else:
                    print("Student", name, "not found.  Spelling error?")
                
            case 5: #sort students by grades
                print("Please give us the subject to sort by.")
                print("The subject may be: Math, Science, English, Dutch, or Arts.")
                category = input("Subject to sort by:\t").lower()
                match category:
                    case "math": list.sort(0)
                    case "science": list.sort(1)
                    case "english": list.sort(2)
                    case "dutch": list.sort(3)
                    case "arts": list.sort(4)
                    case _: print("Error.  Check the spelling of the subject?")
            
            case 6: #save and exit
                runFlag = False
                list.save(filePath)

            case 7: #save without exiting
                runFlag = False

            case _: #user typed a number not in the menu
                print("Invalid choice.  Reprinting options.")  
    
    


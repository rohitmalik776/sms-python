import os
from enum import Enum

class option(Enum):
    Create = 1
    Read = 2
    Update = 3
    Delete = 4
    Exit = 5
class Student:
    def addStudent():
        name = input("Enter name: ")
        rollNo = input("Enter roll no.: ")
        batch = input("Enter batch: ")
        return Student(name, rollNo, batch)
    def __init__ (self, name, rollNo, batch):
        self.name = name
        self.rollNo = rollNo
        self.batch = batch
    def show(self):
        print("name: " + self.name)
        print("roll no.: " + self.rollNo)
        print("batch: " + self.batch)
    def update(self):
        self.name = input("Enter new name: ")
        self.rollNo = input("Enter new roll no.: ")
        self.batch = input("Enter new batch: ")

def saveData(studentArr):
    file = open("database.txt", 'w')
    for i in studentArr:
        file.write(i.name + ';')
        file.write(i.rollNo + ';')
        file.write(i.batch + ';')
        file.write('\n')

def importData(studentArr):
    file = open("database.txt", 'r+')
    for i in file:
        details = i.split(';')
        studentArr.append(Student(details[0], details[1], details[2]))

def printAllStudents(studentArr):
    for i in studentArr:
        i.show()

def deleteStudent(studentArr):
    while(True):
        os.system("cls")
        print("Select index of student to delete")
        print("Enter -1 to go back")
        printAllStudents(studentArr)
        try:
            delIndex = int(input("Your choice: "))
            if(delIndex == -1):
                break
            studentArr.pop(delIndex - 1)
            break
        except TypeError:
            print("Invalid Option")
        except ValueError:
            print("Choose a number please")
        except IndexError:
            print("No such student exists")
        input("press return to continue")

def updateStudent(studentArr):
    while(True):
        os.system("cls")
        print("Select the index of student to delete")
        print("Enter -1 to go back")
        printAllStudents(studentArr)
        try:
            modIndex = int(input("Your choice: "))
            if(modIndex == -1):
                return
            studentArr[modIndex-1].update()
            return
        except TypeError:
            print("Invalid Option")
        except ValueError:
            print("Choose a number please")
        except IndexError:
            print("No such student exists")

mainMenuArr = ["Choose an option:", "1. Add a student", "2. Print all students", "3. Modify a student","4. Delete a student", "5. Exit"]

studentArr = []

importData(studentArr)

while(True):
    os.system("cls")
    for i in mainMenuArr:
        print(i)
    inputNum = input("Your choice: ")

    try:
        inputNum = option(int(inputNum))
    except ValueError:
        print("Invalid option, try again!")
    except TypeError:
        print("Enter a number and try again")

    if(inputNum == option.Create):
        studentArr.append(Student.addStudent())
    elif(inputNum == option.Read):
        for i in studentArr:
            i.show()
    elif(inputNum == option.Update):
        updateStudent(studentArr)
    elif(inputNum == option.Delete):
        deleteStudent(studentArr)
    elif(inputNum == option.Exit):
        saveData(studentArr)
        break
    else:
        print("No such option")
    input("Press return to continue")
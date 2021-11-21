from enum import Enum

class option(Enum):
    Create = 1
    Read = 2
    Update = 3
    Delete = 4

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

studentArr = []

mainMenuArr = ["Choose an option:", "1. Add a student", "2. Print all students", "4. Delete a student"]

def deleteStudent(studentArr):
    while(True):
        print("Select index of student to delete")
        for i in studentArr:
            i.show()
        try:
            delIndex = int(input("Your choice: "))
            studentArr.pop(delIndex - 1)
            break
        except TypeError:
            print("Invalid Option")
        except ValueError:
            print("Choose a number please")
        except IndexError:
            print("No such student exists")

while(True):
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
    elif(inputNum == option.Delete):
        deleteStudent(studentArr)
    else:
        print("No such option")
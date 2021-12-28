# student={"name":"Nobita", "grades":(88,75,95,95,92)};

# def average(sequence):
#     return sum(sequence)/len(sequence)

# print(average(student["grades"]))


# ------re writing the above example using oops ------

class Student:
    def __init__(self,name,grades):  # self is just a variable u can use any name here
        # self.name="Rolf" 
        self.name=name
        # self.grades=(88,75,95,95,92)
        self.grades=grades
    # when defining a method in python class we pass a varibale self which is necessary , so while calling this method we pass on the object created in the method i.e. we pass "student" object
    def average(self):
        return sum(self.grades)/len(self.grades)

# student=Student() 
student=Student("Shizuka",(99,98,97,99,100))
# python creates a new empty container and runs init method , so when function is finished running python gives the value of self to student . so student is now self

print(student.name)
print(student.grades)

print(Student.average(student))
#this syntax is used to call the method average of Student class and we pass on student object created so that it can take place of self. 

print(student.average())
# this is also same as above
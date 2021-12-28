class Person:
    def __init__(self,name,age):  # self is just a variable u can use any name here
        self.name=name
        self.age=age
    #this method is invoked automatically when we print an object i.e. bob
    def __str__(self):
        return f"Person {self.name} is {self.age} years old. "
    #this method is also same , we use this for debugging
    def __repr__(self):
        return f"<Person ( {self.name} {self.age} )>"

bob=Person("Doraemon",100)
print(bob)
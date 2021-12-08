def hello():
    print("hello")
hello()

def user_age_in_months():
    age=input("Enter your age in years: ")
    months=int(age)*12
    print(f"your age is equal to {months} months")

# user_age_in_months()

friends=["Nobita", "Shizuka"]

def add_friends():
    new_friend=input()
    f=friends+[new_friend]
    f=f+["chimpa"]
    print(f)

add_friends()

# x,y are called parameters
def add(x,y):
    pass #it means do nothing
    result=x+y
    print(result)

#arguments
add(4,6)

def say_hello(name,surname):
    print(f"hello,{name} {surname}")

say_hello("Nobita", "Nobi")
#nobita and nobi are known as positional arguments because they are mapped respectively to name and surname 

#keyword or named arguments

say_hello(surname="Nobita", name="Nobi")

#positional arguments go first then keyword arguments can plced
say_hello("Nobi" , surname="Nobita")

#default paramter values in python
def add(x,y=8):
    print(x+y)

add(5)
#default paramters value must go at the end not in the begining

default_y=3
def add(x,y=default_y):
    sum=x+y
    print(sum)

add(3)
default_y=4
add(5)
# it did not update the value of y parameter in function add to 4.
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

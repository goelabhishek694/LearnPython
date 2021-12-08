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


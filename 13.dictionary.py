# list of tuples
users=[
    (0,"Bob","password"),
    (1,"Rolf","rolf123"),
    (2,"Jose","longjose"),
    (3,"Nobita","shizuka"),
]
# for user in users:
#     print(user)
#     print(type(user))
#this is useful if we want to get the information of a user if we know only it's name
user_mapping={user[1] : user for user in users}
print(user_mapping)

#use case 
username_input=input("enter username: ")
password_input=input("Enter password: ")

_, username,password=user_mapping[username_input]
print(f"{username} is the username")
if(password_input==password):
    print(password)
else:
    print("password is incorrect")
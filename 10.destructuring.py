#tuple
t=5,11
print(type(t))

#destrucuturing a tuple
x,y=t
print(x,y)

student_attendance={"Rolf":90, "Anne":70, "Bob":96}

print(student_attendance.items())
#dict-items is the type 
print(type(student_attendance.items()))

# it has noew been converted to type list 
print(type(list(student_attendance.items())))

# we get a list of tuples
print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)

for student,attendance in student_attendance.items():
    print(f"{student}:{attendance}")

person=("bob",32,"Mechanic")
name, _, profession=person
print(name,profession)

head, *tail=[1,2,3,4,5]
print(head)
print(tail)

*head, tail=[5,6,7,8,9]
print(head)
print(tail)



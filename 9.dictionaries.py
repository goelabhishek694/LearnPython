friends={"Rolf":20, "Anne":30}
# accesing a key
age=friends["Anne"]
print(age)
# adding a key
friends["Abhi"]=24
print(friends)

# list of div
friends=[
    {"Name":"Rolf","Age":20},
    {"Name":"Anne","Age":30}
    ]
print(friends[1]["Age"])   

student_attendance={"Rolf":90, "Anne":70, "Bob":96}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}:{attendance}")

if "Bob" in student_attendance:
    print(student_attendance["Bob"])
else:
    print("Bob is not a student in this class")

# attendance_values will contain list of these values 
attendance_values=student_attendance.values()
print(attendance_values) #dict_values([90, 70, 96])

# avg attendanceprint(sum(attendance_values)/len(attendance_values))
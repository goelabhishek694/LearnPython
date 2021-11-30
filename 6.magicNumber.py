number=7

while True:
    user_input=input("If you want to play , enter y , else n : ")
    if user_input=='n':
        break
    # if user_input in ("y","Y","Yes","yes"):
    user_number=input('enter a number ')
    if user_number==number:
        print("Correct number")
    else:
        print("incorrect number")
    


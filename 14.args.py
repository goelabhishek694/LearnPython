def multiply(*args):
    #tuple is printed
    print(args)
    total=1
    for arg in args:
        total=total*arg
    return total


# print(multiply(1,3,5))

def add(x,y):
    return x+y

nums=[2,5]
print(add(*nums))

nums={"x":15,"y":45}
#this format is equal to x=nums["x"], y=nums["y"]
print(add(**nums))

#this is a special syntax, means collect althe positional arguments in this tuple args and also creatte a named argument in the last
def apply(*args, operator):
    if operator=="*":
        # print(*args) #prints 1,2,3,4,5
        # print(args) prints (1, 2, 3, 4, 5)
        return multiply(*args) #passing args will change the behaviour, it will tupple of tupple , so for loop in multiply function will extract a tuple , so tuple multiplied by 1 will return a tuple hence the ans. To overcome this we use *args

    elif operator=="+":
        return sum(args)
    else: 
        return "No valid operator provided to apply()"

print(apply(1,2,3,4,5,operator="*"))


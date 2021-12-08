#lambda functions are those functions which do not have name and are used to return values , used to operate on inputs 

def add(x,y):
    return x+y

print(add(5,7))

#this is how you write lmbda function
add=lambda x,y:x+y
print(add(3,4))

# or
print((lambda x,y:x+y)(5,7))


def double(x):
    return x*2
sequence=[1,2,3,4,5]
doubled=[double(x) for x in sequence]
print(doubled)

doubled=map(double,sequence)
print(doubled)

doubled=[(lambda x:x*2)(x) for x in sequence]
print(doubled)
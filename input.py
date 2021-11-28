name=input()
print(name)
#input function always return a string 
size_in_sqft=input()
# this statement would give error because we r trying to divide string/float
# to overcome we convert it into int
size_in_sqmts=int(size_in_sqft)/10.8
print(size_in_sqmts)

# we can also limit the decimal points
print(f"upto two deciaml points {size_in_sqmts:.2f}")




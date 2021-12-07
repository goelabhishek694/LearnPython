arr=[12,45,67,15,11]
double=[]

for val in arr:
    double.append(val*2)

print(double)
#list comprehension
# what u have to add , the for loop
doubled=[x*2 for x in arr]
print(doubled)

#we want to add the names in another array that starts with B
names=["Bunty", "Saurbh", "Vivek", "Bubly"]
#what u have to add , the for loop , then if loop for condition
starts_b=[name for name in names if name.startswith('B')]
print(starts_b)
#this gives a uique num which corresponds to memory
print(id (starts_b))
b
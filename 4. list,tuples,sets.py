#this is how list is defined
l=["doraemon","shizuka","nobita"]

#this is how tuple is defined
# key difference is that cant ad remove elements is tuple unlike list
t=("doraemon","shizuka","nobita")
# set does not have duplicate element also list and tuples keep the order of element unlike sets
s={"doraemon","shizuka","nobita"}
print(l[1]);
print(t[0]);
print(s);

# list properties
l[0]="gian"
l.append("Sunio")
l.remove("shizuka")
# cannot do this in tuple will give error
t[0]="gian"
l.append("Sunio")

s.add("Sunio")
# cannot add duplicate, it will only print one sunio in set
s.add("Sunio")
print(s)

# set properties 
set1=("Alpha","Beta","Gamma")
set2=("Delta","Zeta")
# .intersection
# .difference
# .union
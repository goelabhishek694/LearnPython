print(5==5)

friends=["A","B"]
abroad=["A","B"]
# The is keyword is used to test if two variables refer to the same object
print(friends==abroad)
print(friends is abroad)

day_of_week=input("Enter a day of week: ").lower()
if day_of_week=="monday":
    print("boring monday")
elif day_of_week=="tuesday":
    print("Boring tuesday")
else: 
    print('more boring week')

# in keyword is used to check for membership i.e. if one thing is inside a tuple set ot list 
# it is also used in strings
set1=("Alpha","Beta","Gamma")
print("Alpha" in set1)

movies_watched=("Matrix","MI-4","Captain America")
movie=input()

if movie in movies_watched:
    print("Already watched this movie")
else:
    print("did not watch this movie")


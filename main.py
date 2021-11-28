x=15
price=9.99
discount=0.2
result=price*(1-discount)
# print(result)

# strings
name="Abhi"
print(name)
# print(name*2)

name="Bob"
greeting="hello Bob"
greeting1= f"hello, {name}"
print(greeting)

# even though name's value is changed this will still print 'hello Bob' 
name="Abhi"
print(greeting1)

# this will print the name of the person dynamically
print(f"hello, {name}") 

# one more way of printing strings dynamically
name="Deepali"
greetings="Hello ,{}"
dynamic_greeting=greetings.format("Deepali")
print(dynamic_greeting)

longer_phrase="Hello {} Today is {}"
lp=longer_phrase.format("Abhi", "sunny day")
print(lp);

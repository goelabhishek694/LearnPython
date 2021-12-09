# <--------------------Packing keyword argument-------------------->

def named_pack(**kwargs):
    print(kwargs)
    print(type(kwargs))


#keyword argument is set, which is then carhed by function as dictionary items. i.e. kwargs keyword packs the keyword arguments into dictionary form
named_pack(name="Bob",age=25)

# <--------------------UnPacking keyword argument-------------------->

def named_unpack(**kwargs):
    print(kwargs)

details={"name":"Bob","age":25}
named_unpack(**details)


#printing the kwargs nicely

def print_nicely(**kwargs):
    named_unpack(**kwargs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_nicely(**details)
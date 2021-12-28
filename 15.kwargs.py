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

# <--------------------Using args and kwargs-------------------->


#positional arguments in args and named arguments in kwargs

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5,name="Bob", age=25)

# it is used to pass unlimited ammount of arguments , this is also done so that these arguments can be further passed to other functions

# e.g.

# def post(url,data=None, json=None, **kwargs):
#     return request('post',url,data=data,json=json,**kwargs)

# in this function we added one more argument i.e. post along with other arguments received, basically to make function arguments dynamic 


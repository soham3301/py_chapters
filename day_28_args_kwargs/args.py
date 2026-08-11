
def function(*args):
    print(args)

function("hello", "I am soham", 24, "Years old")

def k_fucn(**kwargs):
    print(kwargs)

k_fucn(name="Soham", age=34, job="freelancer")

def new_func(*args, **kwargs):
    print(f"Here is the kwargs: {kwargs}")
    print(f"Here is the args: {args}")



new_func(22, 44, "Amitabh")

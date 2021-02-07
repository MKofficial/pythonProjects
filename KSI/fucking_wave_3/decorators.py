def repeat_five(func):
    def inner(param=None):
        for i in range(5):
            func(param)

    return inner


@repeat_five
def hello_world(param):
    print("hello world")


hello_world()

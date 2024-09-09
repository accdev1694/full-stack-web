def announce(f):
    def wrapper():
        print("Here comes a function")
        f()
        print("end")
    return wrapper


@announce
def greeting():
    print("Hello World")
    
greeting()

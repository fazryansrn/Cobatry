def lowercase (func):
    def wrapper ():
        func_ret = func()
        change_to_lowercase = func_ret.lower ()
        return change_to_lowercase
    return wrapper

def UPPERCASE (func):
    def wrapper ():
        func_ret = func()
        change_to_uppercase = func_ret.split ()

        return change_to_uppercase
    return wrapper

@lowercase
@UPPERCASE
def hello_function():
    return 'HELLO WORDL'

print (hello_function())
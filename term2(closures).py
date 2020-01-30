# closures
# wikipidea says, "A closure is a record storing a function together with 
# an environment: a mapping associating each free variable of the function
# with the value or storage location to which the name was bound when the 
# closure was created. A closure, unlike a plain function, allows the 
# function to access those captured variables through the closure's
# references to them, even when the function is invoked outside their scope. "

def outer():
    name = "Shawki"
    def inner():
        print(name) # here the variable is called "free variable" because it doesn't defined in the function, but we can still use that.
    return inner
# we are returning the inner function

func=outer()
# here func variable is a function now.
print(func)
# but it is not outer function it is inner function.
# we can print out just the name of it.
print(func.__name__)
# and execute this variable just like other functions by adding parenthesis.
func()

# but this is pretty interesting. Now we dont have any access with the outer function.
# but our func function which is the inner function can still print the free variable.
# this is what closer is.
# in simple terms, a closer is a inner function which remember that it have access to variables of the local scope where it was created

# this gets more interesting if we add parameters.
def outer_func(msg):
    massage = msg
    def inner_func():
        print(massage) 
    return inner_func

hello_func=outer_func("hello")
hi_func=outer_func("hi")

hello_func()
hi_func()
# here our inner_func still dont need any parameters. So we only need to add blank parenthesis.

import logging
logging.basicConfig(filename="example.log",level=logging.INFO)

def logger(func):#this outer function takes a function as its parameter.
    def log_func(*args):# this outer func takes any number of positional arguement. thats what *args means.
        logging.info(f"Running {func.__name__} with arguements {args}")
        # here we are logging that we are running the function passed in 
        # and its also prints out the arguements that we used with that function.
        print(func(*args))
    return log_func

def add(x,y):
    return x+y
def sub(x,y):
    return x-y

add_logger=logger(add)
sub_logger=logger(sub)

add_logger(3,5)
sub_logger(8,6)

# but we can do that with our original add and sub function too.
# but by creating a closure, we can see a example.log file in our folder.
# and it should logged there that we are running a specific function with specific arguements.

# this closures can be extreamly powerfull and there are countless ways where we can use them.
# now this specific example with logging in python would probably be a better usecase for python decorator.
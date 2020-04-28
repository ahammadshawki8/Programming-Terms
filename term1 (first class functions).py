# FIRST CLASS FUNCTIONS:
# a programming language is said to have first class functions if it treats functions as first class citizens.

# FIRST CLASS CITIZEN (PROGRAMMING):
# a first class citizen (sometimes called first class object) in a programming language is an entity 
# which supports all the operations generally available to other entities. These operations typically 
# include being passed as an arguement, returned from a function and assigned to a variable.

# it actually mean we should be able to treat functions just like any other object or variable.

# ASSIGNED A FUNCTION TO A VARIABLE:
# what does it mean to assign a function to a variable?
# this doen't mean that we are assigning the result of the function.

def square(x):
    return x**2

f=square(5)
print(square)
print(f)
# but we can remove those parenthesis and treat "f" as our square function. Because parenthesis means execute the function.
# we dont want to execute it, we want to "f" equal to square function.
f=square
print(square)
print(f)
# now we can use "f" just like our square function.
print(f(5))

# WHAT IS A HIGHER ORDER FUNCTION?
# if a function accepts other functions as arguement or return function as their results that is called a "Higher Order Function".

# A FUNCTION BEING PASSED BY AN ARGUEMENT:
# very common scenario of this type function is "map" function.
# lets create a map function
def my_map(func,arg_list):
    r_list=[]
    for i in arg_list:
        r_list.append(func(i))
    return r_list
def cube(x):
    return x**3
cubes=my_map(cube,[1,2,3,4,5,6,7]) # here we don't use parenthesis after cube as we are not executing it.
print(cubes)
# default map function
cubes2=list(map(cube,[1,2,3,4,5,6,7]))
print(cubes2)

# RETURN A FUNCTION FROM A FUNCTION:
# this is most complicated and confusing among previous examples.
def logger(msg):
    def log_message():
        print("log:",msg)
    return log_message
log_hi=logger("hi")
log_hi()# it has remembered our initial message that we have passed in the initial logger function.

# why this first class functions are useful?
# lets see some practical examples.
def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag,msg))
    return wrap_text
print_h1=html_tag("h1")
print_h1("Test Headline")# it has print our wrap text function and has remembered initial tag.
print_h1("Another Headline")

print_p=html_tag("p")
print_p("Test Paragraph")
# we can also use this type of functions for logging and python decorator.

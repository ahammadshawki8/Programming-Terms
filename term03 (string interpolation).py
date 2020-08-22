# STRING INTERPOLATION:
# The process of evaluating a string literal containing one or more placeholders,yeilding a result 
# in which the placeholders are replaced with their corresponding values.

name="Shawki"
age=14
greeting="My name is "+name+". I am "+str(age)+" years old."
print(greeting) 
# this is not string interpolation. This is actually string cancatenation.
# but string cancatenation is too messy. 
# Moreover, here we can do mitakes and errors easily which is not good at all.

# so we can use string interpolation
name="Shawki"
age=14
greeting="My name is {}. I am {} years old.".format(name,age)
# here we are using placeholders(curly brackets) within the text ang replacing them with their values.
print(greeting) 
# this is much easier to read. We can read where the placeholders are.
# by using format method first value placed in the index of first placeholder and so on.
# but that is not necessary. we can just:
greeting="I am {age} years old. My name is {name}.".format(name=name,age=age)
print(greeting)
# or we can use placeholders index.
greeting="I am {1} years old. My name is {0}.".format(name,age)
print(greeting)
# so string interpolation is lot easier than cancatenation and it is error free too.
# it is pretty much a templete. this can be great use when we are riceiving values from database.
# again we can write our html code and we can put in this placeholders in web development.


# we can do that with "f" string too.
name="Shawki"
age=14
greeting=f"My name is {name}. I am {age} years old."
print(greeting) 
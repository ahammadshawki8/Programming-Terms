# terms 11
# operators, module and data structures

# operators
# we are dealing with operators whole life.
# operators kind of like functions but they are special functions.
# they take input and gives us back output. they follow a very specific syntax.
# common operators are: +, -, *, /, //, **, %, =, +=, -= etc.

# every single operator operates on some values. the values are called "operand"

# based on operands operators are 3 types.
# 1. urany operator: it have single operand.
#       exp: a++
# 2. binary operator: it have double operand. it is the most common operators.
#       exp: a+b, a-b etc.
# 3. ternary operator: it have triple operand. it is also a famous one in programming.
c=100
a=100
b = 200 if a==c else 300
# here we are operating with tree values.

# based on the position operator are 3 types.
# 1. infix operator: if the operator is situated between the operands.
#       exp: a+b, a-b etc.
# 2. prefix operator: if the operator is situated before the operand.
#       exp: ++a
# 3. postfix or suffix operator: if the operator is situated after the operand.
#       exp: a++

# operator overloading
# it is a very common common thing in on different programming language and it is pretty complex too.
# it gives us the power of manipulating the operators functionality.
# so it is a powerful stuff. when we need the operator to do custom stuff, we are really going to need operator overloading.
# we have descrived much about this topic in magic methods module of oop series.
# lets see a quick look what it is.
class myint:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value - other.value
num1=myint(10)
num2=myint(2)
print(num1+num2)
# it will do substraction instead of addition.


# module
# module have 3 characteristics.
# module should encapsulates complex code functionality,
# it should have an well-defined interface, 
# it should me usable i mean importable and executable in different part of the system.

# module can be of 3 types.
# first one is standerd libraries. they are default built in modules of python.
# second one is third party libraries. Very good developers make this libraries for a certain use.
# third is own module. right now, the file we are working on, is one kind of module of our own.

# we can find all the modules and standerd libraries which we can use in python in this link-
    #https://docs.python.org/3/library/index.html


# data structures & abstract datatype
# abstract datatype is a set of rules of how some things could behave and operate.
# data structure is a concrit implementation of a abstract datatype.

# lets say, we have a abstract datatype like a stack.
# it just defines some behaviour like push, pull, pop etc.
# but there are many ways to implement the stacks behaviors like arrays or linked list.
# and each of those implementation is a data stucture.
# some data structures are more efficient than the other one.

# so in general, in all spaces of programming, when we here the word "abstract", it means there is no implementation at all.
# we should think this is a interface or set of rules to follow.

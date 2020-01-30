# IMMUTABLE:
# an immutable object is an object whose state cannot be modified after it is created.
# MUTABLE:
# this is in contrast of an immutable object, which can be modified after it is created.

a="shawki"
print(a)
# in python, a string is immutable.
# immutable doesn't mean that we can not assign it.
a="john"
print(a)
# here a is immutable. so what's going on here?
#= it is not actually modifing the string object, it is creating a new string object.
# we can see that in detail with id() function.
a="shawki"
print("Address of a    : ",id(a))
a="john"
print("New address of a: ",id(a))
# here we can see that the memory addresses dont match.
# so whenever we change that string object it will create a new object since strings are immutable.
# if we want to modify our string.
#a[0]="J"
#print(a)
# here we are getting a type error.


a=[1,2,3,4,5] # in python, a list is mutable.
print(a)
print("Address of a: ",id(a))
a[0]=6 # here we modified our list.
print(a)
print("Address of a: ",id(a))
# we can see that we are getting same memory address even though we modified our list.

# Why is important to know the diffferences between mutable and immutable object?
#= Aside from just avoiding errors, there is also a problem with memory as well. 
# So something can seem harmless which really end up being really bad in performance.
employees=["Shawki","John","Corey","Steve","Mike"]
output="<uL>\n"
for emp in employees:
    output+="\t<li>{}</li>\n".format(emp)
    print("Address of output is {}".format(id(output)))
output+="</ul>"
print(output)
print("\n")
# this actually look fine. but in production code we may have thousands of code that we are concatenating. So, sometimes that becomes an issue.
# here we can see every time it loops though this object memory address is different. So every time it creates a new string object.
# if we have thousands of emp in our list it will vreate thousands of objects in memory.
# so it is good to keep those differences between mutable and immutable objects.

# top-down vs bottom-up approach

# any algorithm can be designed in 2 approach.
    # 1. top down
    # 2. bottom up
# they are totally opposite of each other.

# TOP DOWN
# it is also known as step wise design.
# top down approach is a recursive type and we used memoization in it to make it efficient.
# here we have a main() function.
# and we divide the functions into many sub functions and devide them againg in sub-sub functions.
# here an overview of the system is formulated without having details of any sub function.
# each sub functions are also defined as the same fashion.
# then we calculate the sub functions and memoize them so that we can use it later.
# after joining the result we return the result of the main() function.

# It is said to be a processing where we know the initial knowledge
# and we have to solve a problem by using our knowledge. 
# first we divide the problems into many parts and use our knowledge to solve many parts in a recursive way.
# and then complete the problem

# C is a Structure base language which is actually mean it is made with top down approch.

# BOTTOM UP
# it is also known as divide and conquer approach.
# here we also have a task. 
# but instead of defining the task as the main() function in first.
# we actually, first calculate what are the sub-task is needed to solve our task.
# then we solve the subtask and combine them to find the main task at last.

# here individual parts of the task are specified in details.
# C++, Java, Python are object oriented language.
# they work with differnt objects and they use bottom up approach.

# lets see an example.
# suppose we went to the cockpit of an aeroplane and we dont know how to use it.
# first it will look like a total mess.
# but if we see it for little time and divide that system into differents parts.
# we will see a stirring we know what it do, we will see some meter, we can also know that these calculates something like speed, temprature, force of wind etc.
# we will also see some handle, we can generalize them to changing some values like the speed of the plane or something like that.
# thus after dividing the cockpit we will able to know what it do quite correctly. 

# difference:

# procedure or structure oriented programming languages like C uses top down approach.
# Object oriented programming language like c++, java, python go after bottom up approach.

# top down approch starts at high level design or development and ends at low level design or developments.
# bottom up approch starts with low level design or development and ends with high level design or developments.

# In top down approach main function is written first and all other functions are infoked from main method.
# In bottom up approach main function is written at last.

# No objects are created.
# Objects are run time entities and are created for method invoking.
# MEMOIZATION:
# first of all, note that it is not momorization.
# memoization is an optimization technique used primarily to speed up computer programs 
# by storing the result of expensive fucntion calls and returning the catched result 
# when the same inputs occur again.

import time
def expensive_func(n):
    print("Computing {}........".format(n))
    time.sleep(1) # here sleep function sleeps our program for 1 sec.
    # time.sleep isn't actually computing anything. But this is kind of artificial expensive function call.
    return n*n

# here we are calling this function four different times.
result=expensive_func(4)
print(result)

result=expensive_func(10)
print(result)
#again doing the same operation.
result=expensive_func(4)
print(result)

result=expensive_func(10)
print(result)
# since expensive_func sleeps 1 sec for every function call then this entire program should take about 4 sec.
# Here we have computed 4 and 10 first time with sleep and that is our atrificial computing time and that fine. 
# Because the first time it sees that it has to do that. But then when we do the same operation second time which we've already run earliar.
# So instead of computing those values again it will be nice if we just remember those answers and remembering the answer is what memorIzation all about. 
# Here we are saving the result to a cache so that whenever we see the expensive function call again with the same values passed in
# then instead of computing of values again we can just return the result that we have already computed from that cache.

# so to do that we can-
import time

expen_cache={} # here we have created a dictionary as cache. 

def expensive_func2(n):
    if n in expen_cache:
        return expen_cache[n]# if the value in dictionary it will return that value with out sleeping.
    print("Computing {}........".format(n))
    time.sleep(1)
    result=n*n
    expen_cache[n]=result # if the value is not in dictionary, it will do that artificial expensive function and retun the value and save the value in the dictionary.
    return result

result=expensive_func2(4)
print(result)

result=expensive_func2(10)
print(result)

result=expensive_func2(4)
print(result)

result=expensive_func2(10)
print(result)

# here it will computed onetime for 4 and one time for 10.
# but second time it wont compute, it will return the value from dictionary.
# and this time memorIzation will cut the computation time of our program in half time of previous program.

# there are more advanced thing that we can do with memorIzation.
# we can set up ways to where it does memorIzation automatically and things like that.
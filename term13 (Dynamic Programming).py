# Dynamic Programming (DP)

# what is dp exactly?
# it is actually very simple technic, even though it might sound difficult.
# it is basically a way of making our algorithm more efficient by storing the intermediate results.
# and it works really well if our algorithm have a lot of repetetive elements.
# so we dont have to repeat those elements over and over again.

# lets see how dp works with fibonacci sequence.

# steps of dp:
    # 1. Recursion
    # 2. Store (Memoization) (top down)
    # 3. Bottom up

# lets first see what a recursive solution might look like.
import time
start1= time.time() # here we are doing this steps just for calculating the runtime we can ignore this steps.
def fib1(n):
    if n==1 or n==2:
        result=1
    else:
        result=fib1(n-1)+fib1(n-2)
    return result

print(fib1(25))
end1=time.time()
runtime1=(end1-start1)*100000
print(runtime1)

# here we have to calculate samething multiple time. this really hamper the efficiency of our code.
# if the arguement is small integer like 5, there will be no problem.
# but if we use large integer like 100, then it will be a graet issue for us.  
# the runtime is increasing exponentially after we increase the value one by one.

# so we need to do some memoization
# first we have to create a memo most like a dictionary and then we will store the value.
memo=dict()
start2= time.time()
def fib2(n,memo):
    if memo.get(n) != None:
        return memo[n]
    else:
        if n==1 or n==2:
            result = 1
        else:
            result=fib2(n-1,memo)+fib2(n-2,memo)
        memo[n]=result
    return result

print(fib2(25,memo))
end2=time.time()
runtime2=(end2-start2)*100000
print(runtime2)
# for time complexity of this solution is increasing multiplication rate instead of exponential rate.

# bottom up approach.
# we may think of another solution for this problem.
# we may think why dont we calculate all the result from 1 to fib(n-1) and then store it first 
# and after that return then result. it is called bottom up.
# it is a great alternative of recursion. it takes little time to execute the operation.
# again it has an advantage over recursion as python gives us recursion error if our arguement is too large (about 1000)

# lets see how it works.
start3= time.time()
def fib3(n):
    if n==1 or n==2:
        return 1
    bottom_up={1:1,2:1}
    for i in range(3,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[n]

print()  
print(fib3(10000))
end3=time.time()
runtime3=(end3-start3)*100000
print()
print(runtime3)
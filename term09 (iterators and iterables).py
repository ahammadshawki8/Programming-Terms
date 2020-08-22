# iterables and iterators
# there are lots of confussion between these two terms.


# Iterables:
# it is something that can be looped over.
# a list is iterable because we can loop over a list.
nums=[1,2,3]
for num in nums:
    print(num)
# we can also loop over strings, dictionaries, tuples, files, generators and all kind of different object.
# so how can we tell something is iterable?
# is something is iterable it needs to have a special method called __iter__
# lets see if our list have this dunder __iter__() method.
# we can do this by dir method.
print(dir(nums))
# yes. our list have this magic method.
# so because of our object has a __iter__ method, we can iterate over or loop over this object.
# it enables us the functionality of iteration, so it is called iterable.
# "iteration" means reading one iterables item one by one.


# Iterator:
# a list is iterable but it is not an iterator.
# but if we run the __iter__() method on our list,it we return us a iterator.
# <list_iterator object at 0x000001CAA83859B0>
print(nums.__iter__())
print(iter(nums))
# so what makes something an iterator?
# an iterator is an object within a state so that is remembers where it is during iteration.
# and iterators also know how to get their next value with a dunder next method.
# so if we look at our dir(list) here is no __next__() method.
# so our list doesn't have a state. It doesn't know how get its next value.
# so therefore it isn't an iterator.
# for example, if we try to print the next value of our list wee will get an error.
#Exception has occurred: TypeError
#'list' object is not an iterator
#print(next(nums))
# but __iter__() method returns an iterator.
# so lets try that.
i_nums=nums.__iter__()
print(next(i_nums))
# now we can use next() function.
# so iter() method just has changed our iterable to an iterator.
print(dir(i_nums))
# we can also see that our new iterator object has __next__() method.

# now if we run this i_nums. we can see that this is an iterator.
print(i_nums) #==><list_iterator object at 0x000002414A7056D8>

# if we run the dir method we can see that it both has the __iter__ and the __next__ method.
# this is prtty confusing that the iterator have the __iter__ method.
# but it is very obious that an iterator is also an iterable. so it wil have __iter__ method.
# So it can be said that ALL ITERATORS ARE ITERABLES WHEREAS NOT ALL ITERABLES ARE ITERATORS.
# but when we run the __iter__ method in an iterable it will give us an iterator.
# Again when we run the __iter__ method in an iterator it will remain same. It will just print out the "self"

# now when we converted our iterable into a iterator we can use the next() func.
print(next(i_nums))
# it can also remember its state of iteration.
print(next(i_nums))

# but if we run it one more time, it will give us an error.
# it will raise an exception called "StopIteration"
#print(next(i_nums))
# so whenever we see an StopIteration exception, that means the iterator has been exhausted and it has no values left to print.
# it will only work if we do it manually like this.
# but if we use next function in the for loop, we wont get a StopIteration error
# because the loop knows how to handle this exception and thus we wont see an error.
# the loop basically do the operation like this:
while True:
    try:
        item=next(i_nums)
        print(item)
    except StopIteration:
        break
# Another characteristics of iterator is that they can only go forward.
# there is no function for pulling it backword, reseting it or making a copy of it.
# we can only go forward by calling next()

# So why any of this really matter? What are the practical examples of usecase of it?
# One example is that we can add this methods to our own classes and make them iterable as well.

# so lets see an exmple.
# lets create a class which behave like a built_in range function.

class MyRange:
    def __init__(self, start, end):
        self.value=start
        self.end=end
    # making the class an iterable with __iter__method.
    def __iter__(self):
        # our iter method has to return an iterator.
        # by that we mean that it has to return an object that has a dunder next method.
        # we can simply create a __next__ method in this class.
        # and for doing that we can simply return the same object from our iterator.
        return self
    # so the object needs to have a __next__ method.
    def __next__(self):
        # now we need to figure out the logic in order for the iterator to step through the values.
        # iterators have a state and they remember where they left of in the iteration.
        # and if there are out of values they raise a StopIteration exception.

        # so first we need to check if there are any more values left.
        # because if we dont have any more values left we dont have to print one.
        if self.value>=self.end:
            raise StopIteration
        current=self.value
        self.value+=1
        return current
        # so each time we run this next method it will come in and get the current value, 
        # increment the old value by one and the return current value.
    # now it should work like an iterator.
    # so to use this lets just create an object.
nums=MyRange(1,10)
#for n in nums:
#    print(n)
# so this object is an iterable because we can use the foor loop.
# and it is also an iterator because it has __next__ method.
# so instead of the for loop we can use __next method.
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# Generators:
# there are another usecase of iterator which is generators.
# Generators are extreamly useful to create easy to read iterators.
# they are lot more like a function.
# bbut instead of returning a result, they yeild a value.
# and when they yeild a value they keep that state until the generator runs again and yeild the next value.
# so generators are iterators as well. But the dunder iter and the dunder next method are cerated automatically.
# we dont have to create them which we have done in the class.

# let us make a generator that does teh exact same thing wj=hich our MyRange class does.
def myRange(start,end):
    current=start
    while current < end:
        yield current
        current +=1
# lets use this generator instead of our class and lets see if we get the same results.
number=myRange(1,10)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
# just like our class we can print the values using for loop as well.
for n in number:
    print(n)

# the generator function is much more readable than the class.

# the last thing about iterator is they dont really need to come to an end.
# they can simply go on forever.
# so as long as there a next value our itarator will keep going to print out them each at a time.
# we can do that by making our while loop true in the generator function.
def myRange2(start):
    current=start# there is no limit so we dont have to put the end param here.
    while True:
        yield current
        current +=1
infinity_loop=myRange2(1)
for values in infinity_loop:
    print(values)
# so this is going to be an infinite loop.
# we can do it by the count function from itertools module.


# so the iterator can go on forever but it still only fetches one value at a time.
# this is really handy when we write memory efficiant program because
# sometimes there were too many values that
# we cant hold them all in the memory if we waant to put them in a list or a tuple.
# but if we use an iterator we can loop over one value at a time untill it is exhausted.

# for example we are working with a password cracker.
# and we wanted to brute force it by checking all of the posiible password using a certain group of characters.
# there will be so many different password patterns that we cant hold them all in a single list.
# our computer will just run out of memory.
# but we could use a iterator to usse all the possible password patterns one at a time.
# that shuld take some time, but our program will not take all the momory of our computer and it wont crash.

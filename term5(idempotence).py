# IDEMPOTENCE:
# the property of certain operations in mathematics and computer science, 
# that can be applied multiple times without changing the result beyond the initial application.
# it means actually "f(f(x))=f(x)"
def add_ten(x):
    return x+10

print(add_ten(10))
print(add_ten(add_ten(10)))
# so this is not idempotence.
# again,
print(abs(-10))
print(abs(abs(-10)))
# so this is idempotence.
# so the simple defination of idempotence is:
# whenever we do something over and over and over and we are doing the same thing,
# if we get the same result every time that is a idempotence.
# it is not necessary to be a function. It can be anything, a statement too.

# actually Http get,put and delete methods are alse idempotence.
# because if we go to an url, no matter how many time we reload the page, everytime it not changing anything.
# but Http push method is not idempotance.

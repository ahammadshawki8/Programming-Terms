# DRY = Don't Repeat Yourself.
# it is a principle of software developmment, aimed at reducing repeatition of information of all kinds.

def homePage():
    print("<div class='header'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

    print("<p> Welcome to our Home Page </p>")

    print("<div class='footer'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

def aboutPage():
    print("<div class='header'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

    print("<p> Welcome to our About Page </p>")

    print("<div class='footer'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

def contactPage():
    print("<div class='header'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

    print("<p> Welcome to our Contact Page </p>")

    print("<div class='footer'>")
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>")
    print("</div>")

# here all the header and footer information we have repeated again and again in every page. So it is not dry.
# it is very difficult to maintain this website.
# if we want to add a new link to the header, we have to do that manually in every page.
# so it would be lot nicer if we do that in one place.

# How can we make the code DRY?
# we can make header and footer function instead of repeating that again and again.
def nav_menu():
    print("<a href='#'>Home</a>")
    print("<a href='#'>About</a>")
    print("<a href='#'>Contact</a>") 

def header():
    print("<div class='header'>")
    nav_menu()
    print("</div>")

def footer():
    print("<div class='footer'>")
    nav_menu()
    print("</div>")

def HomePage():   
    header()
    print("<p> Welcome to our Home Page </p>")
    footer()

def AboutPage():
    header()
    print("<p> Welcome to our About Page </p>")
    footer()

def ContactPage():
    header()
    print("<p> Welcome to our Contact Page </p>")
    footer()
HomePage()
# now we can maintain and update our page easily. It is easy to read too.
# And we can update the code in one place.

# we can use this concept in unit test too.
import helpers_calc as calc
import unittest

class CaclTectCase(unittest.TestCase):
    """Test helpers_calc.py"""
    def setUp(self):
        self.x=10
        self.y=5
    
    def tearDown(self):
        pass
    
    def test_add(self):
        # here everytime we have enter the x and y values. but we can put those in setUp function to make our code dry.
        # now we dont have to write down those values again and again. But we have to write self every where when we used those values.
        self.assertTrue(calc.add(self.x,self.y),self.x+self.y)
    
    def test_sub(self):
        self.assertTrue(calc.sub(self.x,self.y),self.x-self.y)
    
    def test_multiply(self):
        self.assertTrue(calc.multiply(self.x,self.y),self.x*self.y)
    
    def test_devide(self):
        self.assertTrue(calc.devide(self.x,self.y),self.x/self.y)
    
if __name__ == "__main__":
    unittest.main()
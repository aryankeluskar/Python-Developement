# 1. Create a class programmer for storing information of a few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def showInfo(self):
        print(f"{self.name} is working on {self.product} ")
    def __init__(self, name, product):
        self.name=name
        self.product=product

Aryan=programmer("Aryan", "Github")
Aryan.showInfo()

# 2. Write a class calculator capable of finding square, cube, and the square root of a number.
class Calculator:
    def cube(a):
        return a*a*a
    def square(a):
        return a*a
    def sqroot(a):
        return a**0.5
print(Calculator.cube(12))

# 3. Create a class with a class attribute a; create an object from it and set a directly using object.a=0 Does this change the class attribute?


# 4. Add a static method in problem 2 to greet the user with hello.


# 5. Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.


# 6. Can you change the self parameter inside a class to something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and see the effects.


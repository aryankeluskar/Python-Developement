# self parameter:
class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getDetails(self):
        print(f"Salary of {self.name} is ${self.salary}")


aryan = Employee("Aryan Keluskar", 356000)
aryan.getDetails()


# static functions:
# used for non-parameterized object functions
class BestStudios:

    @staticmethod  # Decorater
    def stats():
        print("MARVEL STUDIOS")


first = BestStudios()
first.stats()

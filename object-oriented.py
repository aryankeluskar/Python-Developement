# Procedure Oriented Programming:
a=12
b=33
print("sum =",(a+b))

# Object Oriented Programming:
class Adder:
    def sum(self):
        return self.n1+self.n2

# n1 and n2 are data members
# sum is a member function

num = Adder()
num.n1=234
num.n2=342
print("sum =",num.sum())

# Class has the information to create a valid object, class is a bleprint for an object.
# Object is an instance of the class
# Example: a class is like a application-form, object is a filled-application

# Memory is only allocated after Object Instantiation

class RailwayApplication:
    formType="Railway"
    def printData(self):
        print(f"Name: {self.name}, Train: {self.train}")

aryansApplication= RailwayApplication()
aryansApplication.name="Aryan K"
aryansApplication.train="Shatabdi"
aryansApplication.printData()

# Noun      -> Class      -> Employee
# Adjective -> Attributes -> Name, Designation
# Verbs     -> Functions  -> doWork(), getPromotion()


# Class Attributes    - belongs to class, instead of object. Common values like company name.
# Instance Attributes - belongs to object. Unique values like salary, empno, office name.

class Employee:
    company="A.F.O.G.A Tech" 
    salary=135000
    

aryan=Employee()
aryan.office="Begumpet"
aryan.company="The Techynologion Studios" 
ashrith=Employee()
ashrith.office="SR Nagar"
print("Aryan:",aryan.company," $",aryan.salary," in ",aryan.office, "\nAshrith:", ashrith.company)
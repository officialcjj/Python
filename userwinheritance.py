class User:
    #class attributes
    name = ' '
    email = ' '
    password = ' '
    account = 0

    #class methods
    def login(self):
        entry_email = input("Email: ")
        entry_password =  input("Password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("Invalid email or password")

    #initialize user
    def __init__(self, name = 'Joe', email = 'jm@gmail.com', password = '1234', account = 0):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

class Employee(User):
    base_pay = 11.00
    department = 'General'
    id = '0'
    pin = '0000'

    #polymorph login
    def login(self):
        entry_id = input("Employee ID: ")
        entry_pin = input("Pin: ")
        if (entry_id == self.id and entry_pin == self.pin):
            print("Welcome back, {}".format(self.name))
        else:
            print("Invalid email or password")

class Customer(User):
    mailing_address = ' '
    mailing_list = True

    #polymorph login
    def login(self):
        entry_email = input("Email: ")
        entry_password = input("Password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("Invalid email or password")

print("User Login")    
#initialize new user 
new_user = User()
#login new user
new_user.login()

print("Employee Login")
#login as employee
manager = Employee()
manager.login()

print("Customer Login")
customer = Customer()
customer.login()

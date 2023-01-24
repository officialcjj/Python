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

class Customer(User):
    mailing_address = ' '
    mailing_list = True
    
#initialize new user 
new_user = User()
#login new user
new_user.login()

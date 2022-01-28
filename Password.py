class User:
    #Define the attribute4s of the class
    name = "No name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your emaail: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("you are not authorized for this page.")
#Outside of the class you would create an instance of the User Class
new_user = User()
#Call the login method using the new object
new_user.login()

class Customer:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

class Prefered_Customer(Customer):
    Discount = 20%
    Shipping fee = False 

class Reg_Customer(Customer):
    Discount = 0%
    Shipping fee = True  

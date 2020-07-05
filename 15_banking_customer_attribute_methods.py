# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
    bank = 'ABC Bank'

    def __init__(self, name, address, phone, account_number, balance):
        self.name = name
        self.address = address
        self.phone = phone
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def account_information(self):
        print("Account Information: ")
        print("Name: ", self.name)
        print("Bank Name: ", self.bank)
        print("Account Number: ", self.account_number)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Balance: ", self.balance)

    def account_statement(self):
        print("Balance: ", self.balance)

cust1 = Customer("Dev Adhikari", "Kathmandu", "0123456789", "ABC70001", 1000)
cust1.account_information()
cust1.deposit(2000)
cust1.account_statement()
cust1.withdraw(500)
cust1.account_statement()

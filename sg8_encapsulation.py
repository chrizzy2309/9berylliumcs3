class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number =int(account_number)  # Private attribute and an integer
      
        self.__balance =float(balance) #Private attribute and a float

    @property
    def get_account_number(self): #Define getter method (get_account_number) for self
         return self.__account_number

    @property
    def get_balance(self): #Define getter method (get_balance) for self
        return self.__balance


    def set_account_number(self, account_number:int): # Define setter method (set_account_number) for self
        self._account_number = account_number

    def set_balance(self, balance:float):  #define setter method (set_balance) for self
        self._balance = balance
        if balance < 0:  #check if balance is negative
            print("The balance must be not a negative number.")
                                        
            
a1 = BankAccount( 12345, 1000 )

print("Account 1")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_balance}")

print()

print("Update Balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_balance}")

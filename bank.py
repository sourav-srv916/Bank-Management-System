#                🏦 Bank Management System

# -- Class Creation (BankManagementSystem) --
class BankManagementSystem:
    def __init__(self, account_holder, account_no, pin, balance):
        self.account_holder = account_holder
        self.__account_no = account_no
        self.__pin = pin
        self.__balance = balance
        self.__status = "Active"
        self.__transactions = []

    def deposit(self, pin, amount):
        if self.__pin == pin:
            if amount > 0:
                self.__balance += amount
                print(f"₹{amount}/- credited successfully!")
                print("Current balance:", self.__balance)
                statement = f"Deposited: ₹{amount}/-"
                self.__transactions.append(statement)
            else:
                print("Invalid amount")
        else:
            print("Invalid PIN!")

    def withdraw(self, pin, amount):
        if self.__pin == pin:
            if amount > 0:
                if self.__balance >= amount:
                    self.__balance -= amount
                    print(f"₹{amount}/- debited successfully!")
                    print("Current Balance:", self.__balance)
                    statement = f"Withdrawn: ₹{amount}/-"
                    self.__transactions.append(statement)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid amount")
        else:
            print("Invalid PIN!")

    def transfer(self, pin, amount):
        if self.__pin == pin:
            if amount > 0:
                if self.__balance >= amount:
                    self.__balance -= amount
                    print(f"₹{amount}/- transferred successfully!")
                    print("Current Balance:", self.__balance)
                    statement = f"Transferred: ₹{amount}/-"
                    self.__transactions.append(statement)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid amount")
        else:
            print("Invalid PIN!")

    def check_balance(self, pin):
        if self.__pin == pin:
            print(f"Current Balance: {self.__balance}")
            statement = f"Balance Checked"
            self.__transactions.append(statement)
        else:
            print("Invalid PIN!")

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
            statement = f"PIN Changed"
            self.__transactions.append(statement)
        else:
            print("Invalid PIN")

    def account_details(self, pin):
        if self.__pin == pin:
            print("====== Account Details ======")
            print("Account Holder:", self.account_holder)
            print("Account Number:", self.__account_no)
            print("Current Balance:", self.__balance)
            print("Account Status:", self.__status)
        else:
            print("Invalid PIN")

    def transaction_history(self):
        if not self.__transactions:
            print("No records...")
        else:
            if len(self.__transactions) > 5:
                print("====== Transaction History ======")
                serial_no = 0
                start = len(self.__transactions) - 5
                for no in range(start,start+5):
                    serial_no += 1
                    print(f"{serial_no}. {self.__transactions[no]}")
                print()
            else:
                print("====== Transaction History ======")
                serial_no = 0
                for history in self.__transactions:
                    serial_no += 1
                    print(f"{serial_no}. {history}")
                print()

    def change_account_holder(self, pin, new_name):
        if self.__pin == pin:
            self.account_holder = new_name
            print("Name updated successfully.")
            statement = f"Name Changed"
            self.__transactions.append(statement)
        else:
            print("Invalid PIN")
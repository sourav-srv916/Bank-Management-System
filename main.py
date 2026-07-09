#                🏦 Bank Management System

# -- Importing class from bank.py --
from bank import BankManagementSystem

# -- Importing functions from function.py --
from functions import get_pin, get_amount


# -- Account Creation --
print("==============================")
print("       Create an Account      ")
print("==============================")
# -- Validating Account Holder --
while True:
    acc_holder = input("Account Holder: ").strip()
    if acc_holder.replace(" ", "").isalpha():
        break
    else:
        print("Invalid input! Account holder name must contain only letters.")

# -- Validating Account Number --
while True:
    try:
        acc_no = int(input("Account Number: "))
        break
    except ValueError:
        print("Invalid input! Account number must be a number.")

# -- Validating Create New PIN --
while True:
    try:
        initial_pin = int(input("Create New PIN: "))
        if len(str(initial_pin)) == 4:
            break
        else:
            print("Allow only a 4-digit PIN.")
    except ValueError:
        print("Invalid input! PIN must be a number.")

# -- Validating Initial Deposit Amount --
while True:
    try:
        credit_balance = float(input("Initial Deposit Amount: "))
        break
    except ValueError:
        print("Invalid input! Deposit amount must be a number (e.g., 500 or 500.50).")

print("\nAccount created successfully...")
print()

# -- Object Creation --
cus1 = BankManagementSystem(acc_holder, acc_no, initial_pin, credit_balance)

# -- Menu-driven Navigation --
while True:
    print("==============================")
    print("            XYZ BANK          ")
    print("==============================")
    print(f"Welcome {cus1.account_holder}!")
    print("\t1. Deposit")
    print("\t2. Withdraw")
    print("\t3. Check Balance")
    print("\t4. Change PIN")
    print("\t5. Account Details")
    print("\t6. Transfer Money")
    print("\t7. Transaction History")
    print("\t8. Change Account Holder Name")
    print("\t9. Exit")
    print()

    try:
        option = int(input("Enter your option (1-9): "))

        if option == 1:
            confirm_pin = get_pin()
            while True:
                try:
                    deposit_amt = float(input("Enter Deposit Amount: "))
                    break
                except ValueError:
                    print("Invalid input! Deposit amount must be a number (e.g., 500 or 500.50).")
            print()
            cus1.deposit(confirm_pin, deposit_amt)
            print()

        elif option == 2:
            confirm_pin = get_pin()
            withdraw_amt = get_amount("Withdraw amount")
            print()
            cus1.withdraw(confirm_pin, withdraw_amt)
            print()

        elif option == 3:
            confirm_pin = get_pin()
            print()
            cus1.check_balance(confirm_pin)
            print()

        elif option == 4:
            while True:
                try:
                    ex_pin = int(input("Enter Old PIN: "))
                    if len(str(ex_pin)) == 4:
                        break
                    else:
                        print("Allow only a 4-digit PIN.")
                except ValueError:
                    print("Invalid input! PIN must be a number.")

            while True:
                try:
                    current_pin = int(input("Enter New PIN: "))
                    if len(str(current_pin)) == 4:
                        break
                    else:
                        print("Allow only a 4-digit PIN.")
                except ValueError:
                    print("Invalid input! PIN must be a number.")
            print()
            cus1.change_pin(ex_pin, current_pin)
            print()

        elif option == 5:
            confirm_pin = get_pin()
            print()
            cus1.account_details(confirm_pin)
            print()

        elif option == 6:
            confirm_pin = get_pin()
            transfer_amt = get_amount("Transfer amount")
            print()
            cus1.transfer(confirm_pin, transfer_amt)
            print()

        elif option == 7:
            cus1.transaction_history()
            print()

        elif option == 8:
            confirm_pin = get_pin()
            while True:
                update_name = input("Enter New Name: ").strip()
                if update_name.replace(" ", "").isalpha():
                    break
                else:
                    print("Invalid input! Account holder name must contain only letters.")
            cus1.change_account_holder(confirm_pin, update_name)
            print()

        elif option == 9:
            print("Thank you for using XYZ Bank ATM.")
            print("Have a nice day!")
            break

        else:
            print("Invalid option, Choose between 1-9\n")

    except ValueError:
        print("Invalid input\n")
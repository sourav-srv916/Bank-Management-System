#                🏦 Bank Management System

# -- User PIN checking in Function definition --
def get_pin():
    while True:
        try:
            getting_pin = int(input("Enter PIN: "))
            if len(str(getting_pin)) == 4:
                break
            else:
                print("Allow only a 4-digit PIN.")
        except ValueError:
            print("Invalid input! PIN must be a number.")
    return getting_pin

# -- Withdraw and Transfer in Function definition --
def get_amount(caption):
    while True:
        try:
            get_amt = float(input("Enter Withdraw Amount: "))
            break
        except ValueError:
            print(f"Invalid input! {caption} must be a number (e.g., 500 or 500.50).")
    return get_amt

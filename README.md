# 🏦 Bank Management System

A menu-driven **Bank Management System** developed using **Python** and **Object-Oriented Programming (OOP)**. This project simulates basic banking operations with PIN-based authentication, input validation, transaction history, and encapsulation.

---

## 📌 Features

- ✅ Create a new bank account
- ✅ Deposit money
- ✅ Withdraw money
- ✅ Transfer money
- ✅ Check account balance
- ✅ Change account PIN
- ✅ View account details
- ✅ View recent transaction history
- ✅ Change account holder name
- ✅ Input validation using `try-except`
- ✅ Secure PIN verification
- ✅ Encapsulation using private attributes

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Classes & Objects
- Encapsulation
- Functions
- Lists
- Loops
- Conditional Statements
- Exception Handling

---

## 📂 Project Structure

```
Bank-Management-System/
│
├── bank.py          # BankManagementSystem class
├── functions.py     # Input validation helper functions
├── main.py          # Main application and menu
├── README.md
└── .gitignore
```

---

## 📖 Menu Options

```
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Account Details
6. Transfer Money
7. Transaction History
8. Change Account Holder Name
9. Exit
```

---

## 🔒 OOP Concepts Used

### Classes & Objects
- Created a `BankManagementSystem` class.
- Created objects to represent customer bank accounts.

### Encapsulation
Sensitive information is protected using private attributes.

```python
self.__account_no
self.__pin
self.__balance
self.__status
self.__transactions
```

### Methods
Implemented methods for:

- Deposit
- Withdraw
- Transfer
- Check Balance
- Change PIN
- Account Details
- Transaction History
- Change Account Holder Name

---

## 📋 Input Validation

The project validates:

- Account holder name
- Account number
- 4-digit PIN
- Deposit amount
- Withdrawal amount
- Transfer amount

Exception handling is implemented using `try-except` to prevent invalid user input.

---

## 📜 Transaction History

The application stores every transaction in a list and displays the **last five transactions**.

Example:

```
1. Deposited: ₹500/-
2. Withdrawn: ₹200/-
3. Balance Checked
4. PIN Changed
5. Transferred: ₹1000/-
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/sourav-srv916/Bank-Management-System.git
```

2. Open the project folder

3. Run the application

```bash
python main.py
```

---

## 🎯 Learning Outcomes

This project helped me practice:

- Object-Oriented Programming (OOP)
- Encapsulation
- Menu-driven applications
- Input validation
- Exception handling
- Modular programming
- Git & GitHub workflow

---

## 👨‍💻 Author

**Sourav P**

Aspiring Python Full Stack Developer

Currently learning:
- Python
- HTML
- CSS
- JavaScript
- MySQL
- Django

---

⭐ If you found this project useful, feel free to star the repository!

GitHub: https://github.com/sourav-srv916

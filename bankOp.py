import random

class Bank:
    customers = []

    def create_account(self, account_name, age):
        account_number = random.randint(1000, 9999)
        new_account = AccountOperation(account_name, age, account_number)
        self.customers.append(new_account)
        print(f"Account created successfully.\nAccount Number: {account_number}")

    def login(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                return customer
        return None

    def delete_account(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                self.customers.remove(customer)
                print(f"Account {account_number} deleted.")
                break
        else:
            print("Account not found.")

    def view_profile_details(self, customer):
        print("Profile Details:")
        print(f"Account Name: {customer.account_name}")
        print(f"Account Number: {customer.account_number}")
        print(f"Age: {customer.age}")

    def update_profile_details(self, customer, new_name, new_age):
        customer.account_name = new_name
        customer.age = new_age
        print("Profile updated successfully.")

class AccountOperation:
    def __init__(self, account_name, age, account_number):
        self.account_name = account_name
        self.age = age
        self.account_number = account_number
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount))
        else:
            print("Cannot withdraw, insufficient balance.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance-=amount
            recipient.balance+=amount
            recipient.transactions.append(("Received From "+self.account_name,amount))
            self.transactions.append(("Transfer to " + recipient.account_name, amount))
        else:
            print("Cannot transfer, insufficient balance.")

    def check_balance(self):
        return self.balance

    def account_summary(self):
        print("Account Summary:")
        print(f"Account Name: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("Transactions:")
        for transaction in self.transactions:
            print(f"{transaction[0]}: ${transaction[1]}")

# Main program
my_bank = Bank()

while True:
    print("\nWelcome to My Bank")
    print("""
Choose an Option:
1. Create Account
2. Login
3. Delete Account
4. View Profile Details
5. Update Profile Details
6. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        account_name = input("Enter Account Name: ")
        age = input("Enter Age: ")
        my_bank.create_account(account_name, age)

    elif choice == "2":
        account_number = int(input("Enter Account Number: "))
        customer = my_bank.login(account_number)
        if customer:
            print("Login successful.")
            while True:
                print("""
Choose an Operation:
1. Withdraw
2. Deposit
3. Transfer
4. Check Balance
5. Account Summary
6. Logout
                """)
                operation = input("Enter your choice: ")

                if operation == "1":
                    amount = float(input("Enter amount to withdraw: $"))
                    customer.withdraw(amount)

                elif operation == "2":
                    amount = float(input("Enter amount to deposit: $"))
                    customer.deposit(amount)

                elif operation == "3":
                    recipient_acc_num = int(input("Enter recipient's Account Number: "))
                    recipient = my_bank.login(recipient_acc_num)
                    if recipient:
                        amount = float(input("Enter amount to transfer: $"))
                        customer.transfer(amount, recipient)
                    else:
                        print("Recipient account not found.")

                elif operation == "4":
                    print(f"Balance: ${customer.check_balance()}")

                elif operation == "5":
                    customer.account_summary()

                elif operation == "6":
                    print("Logged out.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Account not found.")

    elif choice == "3":
        account_number = int(input("Enter Account Number to delete: "))
        my_bank.delete_account(account_number)

    elif choice == "4":
        account_number = int(input("Enter Account Number: "))
        customer = my_bank.login(account_number)
        if customer:
            my_bank.view_profile_details(customer)
        else:
            print("Account not found.")

    elif choice == "5":
        account_number = int(input("Enter Account Number: "))
        customer = my_bank.login(account_number)
        if customer:
            new_name = input("Enter new account name: ")
            new_age = input("Enter new age: ")
            my_bank.update_profile_details(customer, new_name, new_age)
        else:
            print("Account not found.")

    elif choice == "6":
        print("Thank you for using My Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

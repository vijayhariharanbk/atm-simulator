class ATM:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your Current Balance is: {self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be positive.")
        else:
            self.balance += amount
            print(f"{amount} is deposited to your account. Your new balance is: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be positive.")
        elif amount > self.balance:
            print("Insufficient fund")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawan successfully. Your current balance is: {self.balance:.2f}")

def atm_menu():
    atm = ATM(initial_balance = 1000)

    while True:
        print("\n----ATM Menu---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number between 1 to 4.")
            continue

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Enter a Valid Amount.")
        elif choice == 3:
            try:
                amount = float(input("Enter the amount for withdrawal: "))
                atm.withdraw(amount)
            except ValueError:
                print("Enter a Valid Amount")
        elif choice == 4:
            print("Thanks for using the ATM. Have a Good Day")
            break
        else:
            print("Invalid choice. Enter a valid input between 1 and 4.")


if __name__ == "__main__":
    atm_menu()

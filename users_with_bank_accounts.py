
class BankAccount:

    bank_name = "Bank Of Chase"
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0, username=""): 
        self.int_rate = int_rate
        self.balance = balance
        self.username = username
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficient Funds: Charging a $5 fee.")
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"user: {self.username}, Balance: ${self.balance}, Interest-rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print(f"Account balance is $0 or Negative, not earning any interest.")
        else:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
            

class User:

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(username= self.name)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Hello: {self.name}")
        self.account.display_account_info()

    def transfer_money(self, amount, target):
        self.account.withdraw(amount)
        target.account.deposit(amount)
        self.display_user_balance()
        target.display_user_balance()

### User activity.        

alex = User("Alex Franco", "alex@python.com")
juan = User("Juan Jones", "juan@python.com")
melanie = User("Melanie Castellanos", "melanie@python.com")
monica = User("Monica Trujillo", "monica@python.com")


alex.make_deposit(100).make_withdrawal(50).display_user_balance()

BankAccount.display_all_accounts()

print
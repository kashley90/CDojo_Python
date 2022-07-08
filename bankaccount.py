class bankaccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        bankaccount.all_accounts.append(self)
    

    def make_deposit(self, amount):
        self.balance += amount
        return self 

    def make_withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

BankofAmerica = bankaccount(0.04,500)
CHASE = bankaccount(0.03,500)

BankofAmerica.make_deposit(200).make_deposit(500).make_deposit(500).make_withdraw(100).yield_interest().display_account_info()

CHASE.make_deposit(2000).make_deposit(500).make_withdraw(500).make_withdraw(100).make_withdraw(250).make_withdraw(150).yield_interest().display_account_info()

bankaccount.print_all_accounts()
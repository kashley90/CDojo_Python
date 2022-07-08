
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
        return f"{self.balance}"
        #change to f-string otherwise error in terminal 
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod #still needed? Ask TA
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        
class User:
    
    def __init__(self,name):
        self.name = name
        self.account = bankaccount(0.03,2000)

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account.display_account_info()}")
        return self
        #maybe right??? Double check Kyle before turning in!!!!
    
    def transfer_money(self,amount,user):
        self.amount += amount
        user.amount -= amount
        self.display_user_balance()
        user.display_user_balance()

Vegeta = User("Vegeta")

Vegeta.account.make_deposit(1500)
Vegeta.display_user_balance()
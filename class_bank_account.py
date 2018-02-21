class Account(object):

    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: %s\nAccount balance: $ %s" % (self.owner, self.balance)


    def deposit(self, deposit):
        self.balance += deposit
        print "Deposit $", deposit, "accepted."
        print "Your balance now is: $", self.balance

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            print "Withdrawal $", withdraw, "accepted."
            print "Your balance now is: $", self.balance
        else:
            print "Funds unavailable!"


owner = "John Smith"
balance = 100
acc = Account(owner, balance)

print acc

acc.deposit(100)
acc.deposit(56)
acc.deposit(200)
acc.withdraw(1000)


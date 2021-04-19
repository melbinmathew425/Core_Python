class bank:
    bname="sbi"#staticvariable declaration
    def newac(self,name,acno):
        self.name=name#instance variable, its used self.
        self.acno=acno
        self.minbalance=5000
        self.balance=self.minbalance
    def deposit(self,amt):
        self.balance+=amt
        print("your",bank.bname," ac has credited with amount :",amt)#when we call static variable, we use 'class_name.var_name'
        print("your total balance is :",self.balance)#when we call instance variable, we use 'self.var_name'
    def withdraw(self,amt):
        if amt > self.balance:
            print("insufficient balance")
        else:
            self.balance-=amt
            print("your ac debited with Rs.",amt)
            print("your final balance is Rs.",self.balance)
obj=bank()
obj.newac("abc",125)
obj.deposit(2000)
obj.withdraw(3000)
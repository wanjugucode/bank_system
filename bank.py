from datetime import datetime
class BankAcc:
  
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.loan=0
        self.statement=[]
    def show_balance(self):
        return f"Hello {self.name} you balance is {self.balance}"

    def withdraw(self,amount):
        if amount>self.balance:
            return f"you can't withdraw {amount} it is below minimum"

        else:
             self.balance-=amount
             return self.show_balance()


    def deposit(self,amount):
        try :
            10+amount
        except TypeError:
            return f"The amount must be a figure"
        if amount<0:  
            return f"you cannot deposit ksh:{amount} it is below minimum" 
        else:
            self.balance+=amount
            now=datetime.now()
            transaction={
                "time":now,
                "amount":50,
                "narration":"deposited in your account"
               }
            self.statement.append(transaction)
            return self.statement

    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Your balance is {self.balance} and You cant't withdrwaw  {amount} it is below minimum"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":70,
                "time":now,
                "narration":" withdrawn from your account"
            }
            self.statement.append(transaction)
            return self.show_balance()

    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return




    def borrow(self,amount):
        self.loan=0
        if amount <0:
            return f"Dear {self.name} you cannot borrow {amount} your amount should be more than a 0."
        elif self.loan>0:
             return f"Dear {self.name} you cannot borrow {amount}.Kindly repay your previous loan"
        elif amount>0.1*self.balance:
                 return f"Dear {self.name} you cannot borrow {amount}.your loan limit is {0.05*self.balance}"
        else:
            loan=amount*0.05
            self.loan=loan
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":3000,
                "time":now,
                "narration":"borrowed "
            }
            self.statement.append(transaction)
            return f"Congulaturation {self.name} you have received a loan of {amount} your loan balance is {loan} and your account balance is {self.balance}"


    def repay(self,amount):
        if amount<=0:
            return f"Dear {self.name} you cannot  pay less than 0"
        elif amount<=self.loan:
            self.loan-=amount
            return f"Dear {self.name} you have payed {amount}"
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)

            now=datetime.now()
            transaction={
                "amount":3000,
                "time":now,
                "narration":"repayed for you loan"
             
                
            }
            self.statement.append(transaction)
            return f" Dear {self.name} you have repaid you loan of sh {amount}.We have deposited {diff} in your account your."
    


    def withdraw(self,amount):
        try:
            self.balance-amount
        except TypeError:
            return f"The amount must be a figure"
    def borrow(self,amount):
        try:
            amount*0.05
        except TypeError:
            return f"The amount must be a figure"
    def repay(self,amount):
        try:
            amount-self.loan
        except TypeError:
            return f"The amount must be a figure"


    def transfer(self,account,amount):
        try:
            amount+10
        except TypeError:
            return f"Amount must be a figure"  
        fee=amount*0.05
        total=amount+fee
        if amount<0:
            return f" Dear {self.name} amount must be greater than 0"
        elif total>self.balance:
            return f"Dear {self.name} you dont have sufficient fund"
        else:
            self.balance-=total
            account.deposit(amount)
            return f"you have transfered {amount} to acc {account} your balance is {self.balance -account}"    
    


class MobileMoneyAccount(BankAcc):
    def __init__(self, name, phone_number,service_provider):
        BankAcc.__init__(name,phone_number)
        self.service_provider=service_provider
    def buy_airtime(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Amount must be a figure"  
        if amount<0:
            return f" Dear {self.name} amount must be greater than 0"
        elif amount>self.balance:
            return f"Dear {self.name} you dont have sufficient fund to buy {amount} worth airtime"
        else:
            self.balance-=amount
            return f"Dear {self.name} you have bought {amount} airtime your new balance is{self.balance}"

    def withdraw(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Amount must be a figure"  
        if amount<0:
            return f" Dear {self.name} amount must be greater than 0"
        elif amount>self.balance:
            return f"Dear {self.name} you insufficient fund to withdraw {amount}"
        else:
            self.balance-=amount
            return f"Dear {self.name} you have withdrawn sh{amount} . your new balance is{self.balance}"


     


              


        





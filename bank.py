from datetime import datetime
class BankAcc:
  
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.loan=0
        self.statement=[]
    def show_balance(self):
        return f"Hello{self.name}you balance is{self.balance}"

    def withdraw(self,amount):
        if amount>self.balance:
            return f"you can't withdraw {amount}it is below minimum"

        else:
             self.balance-=amount
             return self.show_balance()


    def deposit(self,amount):
        if amount<0:  
            return f"you cannot deposit ksh:{amount} it is below minimum" 
        else:
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":50,
                "time":now,
                "narration":"you deposited"}
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
                "narration":"You withdrew"
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
        self.loan+=amount
    def repay(self,amount):
        self.loan-=amount
        return f"Hello have repayed{amount}"
        


    def borrow(self,amount):
        self.loan=0
        if amount <0:
            return f"Dear {self.name} you cannot borrow {amount} your amount should be more than a 0."
        elif self.loan>0:
             return f"Dear {self.name} you cannot borrow {amount}.Kindly repay your previous loan"
        elif amount>0.1*self.balance:
                 return f"Dear {self.name} you cannot borrow {amount}.your loan limit is{0.05*self.balance}"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":3000,
                "time":now,
                "narration":"You have borrowed"
            }
            self.statement.append(transaction)
            return f"{self.show_balance()} and you new  balance is {self.balance}"


    def repay(self,amount):
        if amount<0:
            return f"Dear {self.name} you cannot  borrow less than 0"
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
                "narration":"You have repayed "
            }
            self.statement.append(transaction)
            return f"{self.show_balance()} you new balance is {diff}"


    
              


        





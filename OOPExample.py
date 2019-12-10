class Bank:
    ROI=10.3
    def __init__(self,custname,value):
        self.name=custname
        self.amount=value
    def Deposit(self,val):
        self.amount=self.amount+val
    def Withdraw(self,val):
        self.amount=self.amount-val
    @classmethod
    def Display(cls):
        print (cls.ROI)
    @staticmethod
    def BankInfo():
        print("It is nationalised bank of india");
        print("Location is pune");
def main():
    obj1=Bank("Amar",2000)
    print (obj1.name)
    print (obj1.amount)

    obj1.Deposit(400)
    print (obj1.amount)
    obj1.Withdraw(200)
    print (obj1.amount)
    Bank.Display()
    Bank.BankInfo();
if __name__=="__main__":
    main()

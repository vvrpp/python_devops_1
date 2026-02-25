class BankAccount:
    bankName = "HDFC Bank"
    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.__balance = balance
    # def __del__(self):
    #     print(f"Account closed for {self.name}")
    def show_details(self):
        print("Name: ", self.name)
        print("Account No.: ", self.accno)
        print("Balance: ", self.__balance)
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")
    def getBalance(self):
        return self.__balance
    def withdraw(self,amtWithdraw):
        if amtWithdraw >= self.__balance:
            print("No funds!")
        else:
            self.__balance -= amtWithdraw
abash_acc = BankAccount("Abhash", 123412415324, 20000)
sharath_acc = BankAccount("Sharath", 4121313123, 50000)
abash_acc.withdraw(5000)
abash_acc.__balance = 0
# abash_acc._BankAccount__balance = 0
print(abash_acc.getBalance())
print(abash_acc.__balance)
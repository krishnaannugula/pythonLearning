# customer class

# New savings account

# existing savings account

# bank class

# create a account

# existing account

# dispaly account balance


from abc import ABC, abstractmethod
from random import randint


class Account(ABC):
    @abstractmethod
    def createAccount(self):

        return 0

    @abstractmethod
    def dispalyAccountBalance(self):

        return 0

    @abstractmethod
    def vaildateAccount(self):

        return 0

    @abstractmethod
    def witdrawAmount(self):

        return 0

    @abstractmethod
    def depositAmount(self):

        return 0


class Bank:
    def __init__(self):

        # [key][0] ==> name [key][0] ==> intialDeposit

        # [10001][0] ==> krishna [10001][0] ==> 25000

        # []

        self.accountDetails = {}

    def createAccount(self, name, intialDeposit):

        self.accountNmuber = randint(10000, 99999)

        self.accountDetails[self.accountNmuber] = [name, intialDeposit]

        print("your new account:", self.accountNmuber)

    def vaildateAccount(self, name, accountNmuber):

        if accountNmuber in self.accountDetails.keys():

            if self.accountDetails[accountNmuber][0] == name:

                print("Account number is Authenicated and correct")

                self.accountNmuber = accountNmuber

                return True

            else:

                print("Authentication failed, please check the provided details")

                return False

        else:
            print(
                "Authentication failed, provide account number: {} does not exists ".format(accountNmuber))

            return False

    def witdrawAmount(self, withdralAmount):

        if withdralAmount > self.accountDetails[self.accountNmuber][1]:

            print(
                "Insufficent balance in the account, you have only:",
                self.accountDetails[self.accountNmuber][1],
            )

        else:

            self.accountDetails[self.accountNmuber][1] -= withdralAmount

            # print ("Withdrawl was successful and Available balance in the account:", self.accountDetails[self.accountNmuber][1] )

            print(
                "Withdrawl was successful"
            )  # DRY prinicple do not repeat yourself, as the above balance details is already instansiated in dispalyAccountBalance

            self.dispalyAccountBalance()

    def depositAmount(self, depositedAmount):

        self.accountDetails[self.accountNmuber][1] += depositedAmount

        print(
            "Deposit is successful"
        )  # DRY prinicple do not repeat yourself, as the above balance details is already instansiated in dispalyAccountBalance

        self.dispalyAccountBalance()

    def dispalyAccountBalance(self):

        print(
            "Available balance in the account:",
            self.accountDetails[self.accountNmuber][1],
        )


bank = Bank()


while True:

    print("please select 1 for New Savings Account")

    print("please select 2 for Existing Savings Account")

    print("please select 3 to exit")

    userChoice = int(input())

    if userChoice == 1:

        print("Enter your name:")

        name = input()

        print("Enter intial deposit")

        intialDeposit = int(input())

        bank.createAccount(name, intialDeposit)

    elif userChoice == 2:

        print("Enter your name:")

        name = input()

        print("Enter accountNmuber:")

        accountNmuber = int(input())

        userAuthenticate = bank.vaildateAccount(name, accountNmuber)

        if userAuthenticate is True:

            while True:

                print("Enter 1 for Display your balance")

                print("Enter 2 for Deposit Amount")

                print("Enter 3 for Withdrwal Amount")

                print("Enter 4 to go back to previous menu")

                userInput = int(input())

                if userInput == 1:

                    bank.dispalyAccountBalance()

                elif userInput == 2:

                    print("Please enter Deposit Amount")

                    depositedAmount = int(input())

                    bank.depositAmount(depositedAmount)

                elif userInput == 3:

                    print("please enter amount to withdraw")

                    withdralAmount = int(input())

                    bank.witdrawAmount(withdralAmount)

                elif userInput == 4:

                    break

    elif userChoice == 3:

        quit()

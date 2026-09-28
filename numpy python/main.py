# #calculator design
# print("select your operation:")
# print("1 Add")
# print("2 Substract")
# print("3 Multiply")
# print("4 Division")

# operation=input()

# if operation=="1":
#     num1=input("Enter your number:")
#     num2=input("Enter your another number:")
#     sum=int(num1)+int(num2)
#     print("your sum is:"+str(sum))
    

# elif operation=="2":
#       num1=input("Enter your number:")
#       num2=input("Enter your another number:")
#       diff=int(num1)-int(num2)
#       print("your difference is:"+str(diff))
      

# elif operation=="3":
#       num1=input("Enter your number:")
#       num2=input("Enter your another number:")
#       mul=int(num1)*int(num2)
#       print("your product is:"+str(mul))
      

# elif operation=="4":
#        num1=input("Enter your number:")
#        num2=input("Enter your another number:")
#        div=int(num1)/int(num2)
#        print("your remaminder is:"+str(div))
       
# else:
#     print("enter a valid operation")


# account system

# class Account:
#     def __init__ (self,bal,acc):
#         self.balance=bal
#         self.account=acc


#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"is debited")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"is credited")
#         print("total balance=",self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# #account system

# class Account:
#     def __init__ (self,bal,acc):
#         self.balance=bal
#         self.account=acc


#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"is debited")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"is credited")
#         print("total balance=",self.get_balance())

#     def get_balance(self):
#         return self.bal#account system

# class Account:
#     def __init__ (self,bal,acc):
#         self.balance=bal
#         self.account=acc


#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"is debited")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"is credited")
#         print("total balance=",self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# #object
# acc1=Account(20000000,12345)       #change the values from here for the available account balance and number
# acc1.debit(100000)                #change the debit value
# acc1.credit(10000)                #change the credit value

# # GUESS THE NUMBER

# import random

# target=random.randint(1,100)

# while True:
#     userchoice=int(input("guess the number"))
#     if(userchoice==target):
#         print("sucess:your guess is right")
#         break
#     elif(userchoice<target):
#         print("your guess iss too small : guess a bigger number")
#     else:
#         print("your guess is too big : guess a smaller number ")

# print("---GAME OVER---")


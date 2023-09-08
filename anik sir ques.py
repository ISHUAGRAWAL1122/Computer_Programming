#1
'''
a=int(input("enter age: "))
if 0<=a<=3:
    print("Free")
elif 4<=a<=12:
    print("$10")
elif 13<=a<=17:
    print("$15")
elif 18<=a:
    print("$20")
else:
    print("your age should nopt be negative")
'''
#2
'''
a=input("enter username: ")
b=input("enter password: ")
if len(a)>=5 and len(b)>=8:
    print("Valid")
if len(a)<5:
    print("length of username must be greater than 5")
if len(b)<8:
    print("lengt of password should be greater than 8")
'''
#3
'''
amount=float(input("enter amount: "))
u_r_member=input("enter yes or no")
if amount>=100 and u_r_member.lower()=="yes":
    print("Your amount after discount: ",amount-(amount*(0.1)))
elif u_r_member.lower()=="no":
    print("Since u r not a member the amount You have to pay is:",amount)
else:
    print("Please enter yes or no")
'''

#10

n=int(input("enter number to check: "))
t=n-1
while t>1:
    if n%t==0:
        print("Not Prime")
        break
    t=t-1
else:
    print("Prime")

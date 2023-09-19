#8

n=int(input("enter number "))
t=n
s=0
while n>0:
   r=n%10
   s=s*10+r
   n=n//10
if t==s:
    print("Pallendrome")
else:
    print("not pallendrome")

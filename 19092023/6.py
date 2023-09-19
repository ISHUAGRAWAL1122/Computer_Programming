#6

n=int(input("enter number: "))
a,b=0,1
print(a)
print(b)
while n-2>0:
    c=a+b
    print(c)
    a,b=b,c
    n=n-1

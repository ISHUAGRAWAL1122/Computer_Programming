a=int(input("Enter ending number: "))
s=0
for i in range(1,a+1):
    if i%2==0:
        s=s+i
print("Sum of even numbers from","1","to",a,"is:",s)

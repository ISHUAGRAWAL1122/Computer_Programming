a=int(input("enter first side "))
b=int(input("enter second side "))
c=int(input("enter third side "))
if a+b>c and a+c>b and b+c>a:
    d=0
    if a==b:
        d=d+1
    if a==c:
        d=d+1
    if b==c:
        d=d+1
    if d==0:
        print("Scalene Triangle")
    if d==1:
        print("Isoceles Triangle")
    if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2):
        print("Right angled triangle")
else:
    print("triangle is not possible")

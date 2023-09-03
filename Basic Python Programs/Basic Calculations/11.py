m=int(input("enter amount "))
m=m-100
a=m//2000
b=(m-(a*2000))//500
c=(m-(a*2000+b*500))//100
print("2000:-",a)
print("500:-",b)
print("100:-",c+1)

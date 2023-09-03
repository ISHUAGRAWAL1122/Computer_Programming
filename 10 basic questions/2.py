a=float(input("Enter temperature:- "))
b=input("Enter you temperature type:- ")
if b=="f" or b=="F":
    c=(a-32)*(5/9)
    print("Temperature in celcius:-",c)
    print("Temoperature in Kelvin:-",c+273.15)
elif b=="c" or b=="C":
    c1=((9/5)*a)+32
    c2=(c1-32)*(5/9)
    print("Temperature in Fahrenheit:-",c1)
    print("Temoperature in Kelvin:-",c2+273.15)
elif b=="k" or b=="K":
    c1=a-273.15
    c2=(c1-32)*(5/9)
    print("Temperature in celcius:-",c1)
    print("Temoperature in Fahrenheit:-",c2)

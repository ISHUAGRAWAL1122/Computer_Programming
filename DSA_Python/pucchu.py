def isha(d,n):
    for i in range(n):
        nm=input("endfsdfter name")
        sid=int(input("enter studentid"))
        r_no=int(input("roll no:"))
        contact=int(input("enter contact no."))
        email=input("enter email")
        d[nm]=[sid,r_no,contact,email]
    return d
if "__name__"=="__main__":
    print("hello")
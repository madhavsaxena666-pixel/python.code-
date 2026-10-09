a=int(input("ENTER YOUR AMOUNT OF BILL:\n"))
b=input("ARE YOU A PREMIUM CUSTOMER:\n")
if b=="YES":
    print("YOU DON'T NEED TO PAY ANY DELIVERY CHARGES SO YOU HAVE TO PAY:",a )
else:
    if a<300:
        x=a+50
        print("YOU HAVE TO PAY", x , "AS TOTAL BILL")
    elif a>=300 and a<=599:
        y=a+30
        print("YOU HAVE TO PAY", y , "AS TOTAL BILL")
    else:
        print("YOU HAVE TO PAY", a , "AS TOTAL BILL")

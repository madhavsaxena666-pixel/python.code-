a=int(input("ENTER BILL:\n"))
b=0
if a<=100:
    x=a*5
    b=x
elif a>100 and a<=200:
    x=a-100
    b=x*7+500
else:
    x=a-200
    b=x*10+500+700
if b>2000:
    y=b*5/100
    c=y+b
    print("YOUR TOTAL BILL IS:",c)
else:
    print("YOUR TOTAL BILL IS",b)

a=int(input("ENTER THE AMOUNT OF BILL:\n"))
if(a<=300):
    b=a+50
    print("YOUR TOTAL FOOD BILL INCLUDIING DELIVERY CHARGES IS:\n",b)
elif(a>=300 and a<=599):
    c=a+20
    print("YOUR TOTAL FOOD BILL INCLUDING DELIVERY CHARGES IS:\n",c)
elif(a>=600):
    print("YOUR TOTAL FOOD BILL INCLUDING DELIVERY CHARGES IS:\n",a)

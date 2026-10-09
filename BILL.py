a=int(input("ENTER THE AMOUNT OF BILL:\n"))
c=input("ENTER THE CUPON:\n")
if(a>=500):
    print(c)
elif(a<500):
    print("YOU CAN'T USE ANY CUPON")
elif(c==SAVE10):
    print("YOU CAN HAVE 10% DISCOUNT")
elif(c==SAVE20):
    print("YOU CAN HAVE 20% DISCOUNT")
elif(a<500):
    print("YOU CAN'T USE ANY CUPON")
else:
    print("INVALID CUPON")
    

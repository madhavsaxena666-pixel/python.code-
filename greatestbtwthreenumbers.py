a=int(input("ENTER THE FIRST NUMBER:"))
b=int(input("ENTER THE SECOND NUMBER:"))
c=int(input("ENTER THE THIRD NUMBER:"))
if(a>b and a>c):
    print(a,"IS THE GREATEST NUMBER AMONG TWO",b,"and",c)
elif(b>a and b>c):
    print(b,"IS THE GREATEST NUMBER AMONG TWO",a,"and",c)
elif(c>a and c>b):
    print(c,"IS THE GREATEST NUMBER AMONG TWO",a,"and",b)
elif(a==b and b==c):
    print("ALL THREE NUMBERS ARE EQUAL")


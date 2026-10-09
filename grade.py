a=int(input("Enter the MARKS of 1st SUBJECT:\n"))
b=int(input("Enter the MARKS of 2nd SUBJECT:\n"))
c=int(input("Enter the MARKS of 3rd SUBEJCT:\n"))
d=int(input("Enter the MARKS of 4th SUBJECT:\n"))
e=int(input("Enter the MARKS of 5th SUBJECT:\n"))
tm=a+b+c+d+e
per=(tm*100)/500
print("Total Marks=",tm)
print("PERCENTAGE=",per)
if(per>=80):
    print("Grade A")
elif(per>=70):
    print("Grade B")
elif(per>=60):
    print("Grade C")
elif(per>=60 and per<60):
    print("Grade D")
else:
    print("Grade E")

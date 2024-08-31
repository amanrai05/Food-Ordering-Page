a=input("enter the product name ")
b=int(input("enter the amount of product"))
c1=1.20
c2=1.50
c3=1.80
c4=2.00
if(b<=200):
    bill=b*c1
elif (b>200 and b<=400):
    bill=b*c2
elif (b>400 and b<=600):
    bill=b*c3
else: 
    bill=b*c4
if   (bill>0):
    bill=bill+150*bill
else:
    bill=100
print(bill)

sal=int(input("enter the salary"))
if(sal<=150000):
    print("your income tax is 0")
if(150000<sal<=300000):
    tax=(20/100)*sal
    print("your income tax is ",tax)    
else:
    tax=(30/100)*sal
    print("your income tax is ",tax)    
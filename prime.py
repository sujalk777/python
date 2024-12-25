print("the prime number between 102 to 156 are:")
for x in range(102,157,1):
    flag=1
    for i in range(2,x):
        if(x%i==0):
            flag=0
            break
    if(flag==1):
        print(x)    
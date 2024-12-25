x=1
print("the multiple of 5 and 7")
flag=1
while(x<52):
    if(x%5==0 and x%7==0):
        flag=0
        
    if(flag==0):
        print(x)
        break
    x+=1            
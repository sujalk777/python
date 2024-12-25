num=0
n=0
while(num<=20):
    n1=n
    a=[]
    while(n1>0):
        a.append(n1%10)
        n1//=10
    summation=0
    for i in a:
        summation+=i**len(a)
    if(summation==n):
        print(n)
        num+=1


            

    
    
    
    
    
    
a=int(input("enter the first side of the triangle"))
b=int(input("enter the second side of the triangle"))
c=int(input("enter the third side of the trainagle"))
if(c<a+b and b<a+c and a<b+c):
    print("these dimension can form a triangle")
else:
    print("triangle not possible")    
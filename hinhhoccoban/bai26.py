a,b,c=map(int,input().split())
if(a==b and a==c):
    print("Tam giac deu")
elif(a==b or a==c or b==c):
    print("Tam giac can")
elif(a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
    print("Tam giac vuong")
else:
    print("Tam giac thuong")

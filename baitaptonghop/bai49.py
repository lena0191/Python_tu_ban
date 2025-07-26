a,b=map(int,input().split())
s=input()
if(s=='+'):
    print(a+b)
elif(s=='-'):
    print(a-b)
elif(s=='*'):
    print(a*b)
else:
    if(b!=0):
        print(a/b)
    else:
        print("Syntax error")

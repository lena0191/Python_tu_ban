a,b=map(int,input().split())
while(b>0):
    du=a%b
    a=b
    b=du
print(a)

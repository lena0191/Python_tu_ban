n=int(input())
if(n==0):
    print(0)
else:
    s=""
    while(n>0):
        s=str(n%2)+s
        n//=2
    print(s)

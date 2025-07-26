n=int(input())
so=0
m=n
while(n>0):
    so=so*10+n%10
    n//=10
if(so==m):
    print("La so doi xung")
else:
    print("Khong la so doi xung")

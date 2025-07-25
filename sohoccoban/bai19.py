n=int(input())
tong=0
for i in range (1,n):
    if(n%i==0):
        tong+=i
if(tong==n):
    print("La so hoan hao")
else:
    print("Khong la so hoan hao")

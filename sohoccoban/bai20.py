n=int(input())
f=[0]*n
f[0]=0
f[1]=1
for i in range (2,n):
    f[i]=f[i-1]+f[i-2]
for i in range (n):
    print(f[i],end=' ')

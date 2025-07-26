t,n=map(int,input().split())
def nhuan(n):
    if(n%4==0):
        if(n%100==0):
            if(n%400==0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
a=[0]*13
a[1]=a[3]=a[5]=a[7]=a[8]=a[10]=a[12]=31
a[2]=28+nhuan(n)
a[4]=a[6]=a[9]=a[11]=30
print(a[t])

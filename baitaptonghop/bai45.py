a,b=map(int,input().split())
def ucln(a,b):
    while(b>0):
        du=a%b
        a=b
        b=du
    return a
print(ucln(a,b),a//ucln(a,b)*b)

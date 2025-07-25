n=int(input())
def snt(x):
    if( x==2 or x==3):
        return 1
    if(x<2 or x%2==0 or x%3==0):
        return 0
    i=5
    while(i*i<=x):
        if(x%i==0 or x%(i+2)==0):
            return 0
        i+=1
    return 1
if(snt(n)):
    print("La so nguyen to")
else:
    print("Khong la so nguyen to")
    

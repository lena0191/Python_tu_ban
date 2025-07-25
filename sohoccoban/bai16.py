n=int(input())
def tongcs(x):
    tong=0
    while(x>0):
        tong+=x%10
        x//=10
    return tong
print(tongcs(n))

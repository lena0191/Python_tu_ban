n=int(input())
def tongcs(x):
    tong=0
    while(x>0):
        print(x%10,end='')
        x//=10
tongcs(n)

n=int(input())
def xh(n):
    if(n>=9):
        return("Xuat sac")
    elif(n>=8):
        return("Gioi")
    elif(n>=6.5):
        return("Kha")
    elif(n>=5):
        return("Trung binh")
    return("Yeu (em rat nhieu)")
a=list(map(float,input().split()))
tong=0
for i in range (n):
    tong+=a[i]
print(f"Diem: {tong/n:.2f}, Xep loai: {xh(tong/n)}")

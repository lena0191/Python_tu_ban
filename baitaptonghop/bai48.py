import random
t=random.randint(1,100)
dem=0
while(True):
    n=int(input())
    dem+=1
    if(n==t):
        print("Dung roi! Ban da doan trung sau {dem} lan.")
        break
    if(n<t):
        print("Lon hon")
    else:
        print("Nho hon")
    

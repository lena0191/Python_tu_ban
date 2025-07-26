n=int(input())
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("Nam nhuan")
        else:
            print("Khong phai nam nhuan")
    else:
        print("Nam nhuan")

else:
    print("Khong phai nam nhuan")
            

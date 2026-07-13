a=1
while(a<=100000):
    print("Welcome Hasan Bhai",a)

    a+=1

finalBill=0
while True:
    userItem=input("Enter Your Item\n")
    userPrice=int(input("Enter Your Price\n"))
    if userItem=="closed":
        break
    else:
        finalBill+=userPrice

print("Your Total Bill is :",finalBill)

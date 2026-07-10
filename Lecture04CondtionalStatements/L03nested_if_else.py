name= input("Enter Your Name Here\n")
email= input("Enter Your Email Here\n")
password= input("Enter Your Password Here\n")
contact= input("Enter Your Contact Here\n")


print("Account Successfully Created")

loginEmail= input("Enter Your Login Email Here\n")
loginPassword= input("Enter Your Login Password Here\n")



if email==loginEmail and password== loginPassword:
    print("Welcome ", name)

    year=float(input("Enter Your Year"))
    if year % 4==0:
        print("Leap Year")
    else:
        print("Is not a Leapyear")


    

else:
    print("Incorrect Email Or Password")
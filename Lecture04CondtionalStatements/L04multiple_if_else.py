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



english=float(input("Enter Your English Marks \n"))
mathematics=float(input("Enter Your Math Marks \n"))
islamicStudies=float(input("Enter Your Islamic Studies Marks\n"))
ai=float(input("Enter Your AI Marks \n"))




obtained_Marks=english+mathematics+islamicStudies+ai

print("Obtained Marks", obtained_Marks)


percentage=obtained_Marks/400*100



print("Percentage",percentage)



if percentage <=100 and percentage>=80:
    print("Grade A1")
elif percentage <=79 and percentage >=70:
    print("Grade A")
elif percentage <=69 and percentage >=60:
    print("Grade B")
elif percentage <=59 and percentage >=50:
    print("Grade C")
elif percentage <=49 and percentage >=40:
    print("Grade D")
else:
    print("Jinab Ghar bethen")
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
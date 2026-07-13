# for  i  in range(1,11,2):
#     print("Welcome to MITI",i)



birthYear= int(input("Enter Your Birth Year\n"))
currentYear=int(input("Enter Your Current Year\n"))
meraCounter=0
for i in range(birthYear,currentYear):

    if i % 4==0:
        # meraCounter=meraCounter+1
        meraCounter+=1
        print("Leap Year",i)
    else:
        print("Is Not Leap Year ", i)


print("Total Leap years ",meraCounter)
Name=str(input("Name of a Student: "))
sub1=int(input("Advance Maths: "))
sub2=int(input("Physics: "))
sub3=int(input("Bio-Chemistry: "))
sub4=int(input("Biology: "))
sub5=int(input("English: "))
Total=sub1+sub2+sub3+sub4+sub5
print("Total Score: ",Total)
percentage=(Total/500)*100
print("Percentage:",percentage,"%")
# percentage=int(input("Enter Percentage:"))
if percentage>=80 and percentage<=100:
    print("The Grade is A")
elif percentage>=60 and percentage<80:
    print("The Grade is B")
elif percentage>=35 and percentage<60:
    print("The Grade is C")
else:
    print("Fail")
    

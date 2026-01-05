marks1 = int(input("Enter Marks of subject 1: "))
marks2 = int(input("Enter Marks of subject 2: "))
marks3 = int(input("Enter Marks of subject 3: "))

total_percentage = (marks1 + marks2 + marks3)/3
print(total_percentage)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ) :
    print("you are pass")
else:
    print("failed! Try again next year")

#Kaeden Goode
#9//22/2026
#CTI-110-0001
#P3HW1

#grade input

grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

gradeList = [grade1, grade2, grade3, grade4, grade5, grade6]

#Mathy Math Stuff
gradeLow = min(gradeList)
gradeHigh = max(gradeList)
gradeSum = sum(gradeList)
gradeAvg = gradeSum/len(gradeList)
#=======================================================

if gradeAvg < 60:
    myGrade = "F"
elif gradeAvg < 70:
    myGrade = "D"
elif gradeAvg < 80:
    myGrade = "C"
elif gradeAvg < 90:
    myGrade = "B"
else:
    myGrade = "A"

#=======================================================
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{gradeLow:<40,.2f}")
print(f"{'Highest Grade:':<20}{gradeHigh:<40,.2f}")
print(f"{'Sum of Grades:':<20}{gradeSum:<40,.2f}")
print(f"{'Average:':<20}{gradeAvg:<40,.2f}")
print("-------------------------------")
print(f"{'Your grade is:':<20}{myGrade:<40}")
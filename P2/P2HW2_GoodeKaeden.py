#Kaeden Goode
#9//22/2026
#CTI-110-0001
#P2HW2

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

print("\n------------Results------------")
print(f"Lowest Grade: \t    {gradeLow:.2f}")
print(f"Highest Grade: \t    {gradeHigh:.2f}")
print(f"Sum of Grades: \t    {gradeSum:.2f}")
print(f"Average: \t    {gradeAvg:.2f}")
print("-------------------------------")
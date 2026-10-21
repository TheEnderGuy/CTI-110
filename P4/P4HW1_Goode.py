# Kaeden Goode
# Oct 21, 2026
# P4HW1
# Loops, Loops, More Loops

count = int(input("How many numbers would you like to enter: "))
total = 0
scores = []

for i in range(count):
    
    score = int(input("\nEnter score #" + str(i+1) + ": "))
    
    while score < 0 or score > 100:
        
        print("Invalid Score Entered!!!\nScore should be between 0 and 100.")
        score = int(input("\nEnter score #" + str(i+1) + " again: "))
        
    total = total + score
    scores.append(score)


avg = total / len(scores)
low = min(scores)

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else: grade = "F"

# Apparently lists cannot be formatted unless you convert them to strings (Gives typeError)
print("\n\n-----------------Results-----------------")
print(f"{'Lowest Score':<20}: {low:<20,.2f}")
print(f"{'Modified List':<20}: {str(scores):<20}")
print(f"{'Scores Average':<20}: {avg:<20,.2f}")
print(f"{'Grade':<20}: {grade:<20}")
print("-----------------------------------------")
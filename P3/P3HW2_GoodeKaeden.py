# Kaeden Goode
# 10/11/2026
# P3HW2
# More decision structures

overtimeRate = 1.5
baseHours = 40

overtimePay = 0
overtimeHours = 0


name = input("Enter employee\'s name: ")
hours = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee\'s pay rate: $"))



if hours > 40:
    overtimeHours = hours - baseHours
    
    overtimePay = overtimeHours * payRate * overtimeRate
    
    basePay = baseHours * payRate
    
    finalPay = basePay + overtimePay
    
    
    

else:
    basePay = hours * payRate
    finalPay = basePay
    

print("----------------------------------------")
print(f"{'Employee name: ':<30}{name:<31}\n")

print(f"{'Hours Worked':<16}{'Pay Rate':<16}{'OverTime':<16}{'OverTime Pay':<16}{'RegHour Pay':<16}{'Gross Pay':<16}")
print("-" * 92)
print(f"{hours:<16}${payRate:<15,.2f}{overtimeHours:<16,.1f}${overtimePay:<15,.2f}${basePay:<15,.2f}${finalPay:<15,.2f}")



    


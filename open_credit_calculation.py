#----------------------OPEN CREDIT CGPA SYSTEM

dept = input("Please Enter Department (CSE/EEE/BBA/DS/ME/CE/ICT): ").upper()

total_point = 0
total_credit = 0

if dept == "CSE":
    subjects = 4
elif dept == "EEE":
    subjects = 3
elif dept == "BBA":
    subjects = 3
elif dept == "DS":
    subjects = 4
elif dept == "ME":
    subjects = 3
elif dept == "CE":
    subjects = 4
elif dept == "ICT":
    subjects = 3
else:
    print("Invalid Department")
    exit()

for i in range(subjects):
    print("Subject", i + 1)

    class_test = float(input("Class Test Marks (out of 10): "))
    mid_term = float(input("Mid Term Marks (out of 40): "))
    final_term = float(input("Final Term Marks (out of 50): "))

    total = class_test + mid_term + final_term

    if total >= 90:
        gp = 4.00
    elif total >= 80:
        gp = 3.75
    elif total >= 70:
        gp = 3.50
    elif total >= 60:
        gp = 3.00
    elif total >= 50:
        gp = 2.50
    elif total >= 40:
        gp = 2.00
    else:
        gp = 0.00

    if i == 0:
        credit = 4
    elif i == 1:
        credit = 3
    elif i == 2:
        credit = 2
    else:
        credit = 1
        
    total_point = total_point + gp * credit
    total_credit = total_credit + credit

cgpa = total_point / total_credit
print(f"Your CGPA is = {round(cgpa, 2)}")


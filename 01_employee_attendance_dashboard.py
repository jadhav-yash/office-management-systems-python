employees = {
    "Emp01" : {
        "emp_name" : "Aditya Nair",
        "department" : "Finance",
        "salary" : 30000,
        "absent_days" : 4,
        "deduction_per_day" : 1000
    },

    "Emp02" : {
        "emp_name" : "Raj Malhotra",
        "department" : "Developer",
        "salary" : 45000,
        "absent_days" : 6,
        "deduction_per_day" : 1500
    },

    "Emp03" : {
        "emp_name" : "Meera Joshi",
        "department" : "IT",
        "salary" : 60000,
        "absent_days" : 5,
        "deduction_per_day" : 2000
    },

    "Emp04" : {
        "emp_name" : "Priya Patel",
        "department" : "Marketing",
        "salary" : 15000,
        "absent_days" : 3,
        "deduction_per_day" : 500
    }
}

total_days = 30

for emp_id, details in employees.items():
    present_days = total_days - details["absent_days"]
    deduction = details["absent_days"] * details["deduction_per_day"]
    attendance_percentage = (present_days / total_days) * 100
    final_salary = details["salary"] - deduction

    details["present_days"] = present_days
    details["deduction"] = deduction
    details["attendance_percentage"] = round(attendance_percentage,2)
    details["final_salary"] = final_salary

print("=================================================")
print("          Employee Attendance Dashboard          ")
print("=================================================")

emp_list = ["Emp01","Emp02","Emp03","Emp04"]
print("Active Employee ID's List : ", emp_list)
print()

emp_id = input("Enter the Employee ID to get attendance details from the list: ").strip()
print()

print("==================================================")
print("                 Employee Details                 ")
print("==================================================")

if emp_id == "Emp01" :
    for key,value in employees["Emp01"].items():
        print(key,":",value)

elif emp_id == "Emp02" :
    for key,value in employees["Emp02"].items():
        print(key,":",value)

elif emp_id == "Emp03" :
    for key,value in employees["Emp03"].items():
        print(key,":",value)

elif emp_id == "Emp04" :
    for key,value in employees["Emp04"].items():
        print(key,":",value)

else :
    print("Invalid Employee ID !!!")
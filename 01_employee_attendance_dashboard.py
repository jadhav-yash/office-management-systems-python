absent_days_01 = 4
present_days_01 = 30 - absent_days_01
emp_details_01 = {
    "emp_name" : "Aditya Nair",
    "emp_id" : "Emp01",
    "department" : "Finance",
    "salary_details" : {
        "salary" : 30000,
        "deduction" : absent_days_01 * 1000
    },
    "present_days" : present_days_01,
    "absent_days" : absent_days_01,
    "attendance_status" : (present_days_01 / 30) * 100
}

absent_days_02 = 6
present_days_02 = 30 - absent_days_02
emp_details_02 = {
    "emp_name" : "Raj Malhotra",
    "emp_id" : "Emp02",
    "department" : "Developer",
    "salary_details" : {
        "salary" : 45000,
        "deduction" : absent_days_02 * 1500
    },
    "present_days" : present_days_02,
    "absent_days" : absent_days_02,
    "attendance_status" : (present_days_02 / 30) * 100
}

absent_days_03 = 5
present_days_03 = 30 - absent_days_03
emp_details_03 = {
    "emp_name" : "Meera Joshi",
    "emp_id" : "Emp03",
    "department" : "IT",
    "salary_details" : {
        "salary" : 60000,
        "deduction" : absent_days_03 * 2000
    },
    "present_days" : present_days_03,
    "absent_days" : absent_days_03,
    "attendance_status" : (present_days_03 / 30) * 100
}

absent_days_04 = 3
present_days_04 = 30 - absent_days_04
emp_details_04 = {
    "emp_name" : "Priya Patel",
    "emp_id" : "Emp04",
    "department" : "Marketing",
    "salary_details" : {
        "salary" : 15000,
        "deduction" : absent_days_04 * 500
    },
    "present_days" : present_days_04,
    "absent_days" : absent_days_04,
    "attendance_status" : (present_days_04 / 30) * 100
}

print("=======================================")
print("     Employee Attendance Dashboard     ")
print("=======================================")

emp_list = ["Emp01","Emp02","Emp03","Emp04"]
print("Active Employee ID's List : ", emp_list)
print()

emp_id = input("Enter the Employee ID to get attendance details from the list: ")
print()

if emp_id == "Emp01" :
    for key,value in emp_details_01.items():
        print(key,":",value)

elif emp_id == "Emp02" :
    for key,value in emp_details_02.items():
        print(key,":",value)

elif emp_id == "Emp03" :
    for key,value in emp_details_03.items():
        print(key,":",value)

elif emp_id == "Emp04" :
    for key,value in emp_details_04.items():
        print(key,":",value)

else :
    print("Invalid Employee ID !!!")
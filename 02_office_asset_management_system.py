laptop_avail = 14
projector_avail = 0
keyboard_avail = 32
headphone_avail = 26
office_furniture_avail = 47

laptop_details = {
    "asset_name" : "Laptop",
    "asset_id" : "lap279",
    "emp_details" : {
        "emp_assigned" : "Rahul Deshmukh",
        "emp_id" : "emp01",
        "emp_dept" : "Developer"
    },
    "purchase_price" : 70000,
    "warranty_status" : "5 years", 
    "asset_avail" : laptop_avail
}

projector_details = {
    "asset_name" : "Projector",
    "asset_id" : "pro618",
    "emp_details" : {
        "emp_assigned" : "Ananya Rao",
        "emp_id" : "emp02",
        "emp_dept" : "Marketing"
    },
    "purchase_price" : 5000,
    "warranty_status" : "3 years", 
    "asset_avail" : projector_avail
}

keyboard_details = {
    "asset_name" : "Keyboard",
    "asset_id" : "key937",
    "emp_details" : {
        "emp_assigned" : "Vikram Singh",
        "emp_id" : "emp03",
        "emp_dept" : "Gaming"
    },
    "purchase_price" : 700,
    "warranty_status" : "1 years", 
    "asset_avail" : keyboard_avail
}

headphone_details = {
    "asset_name" : "Headphone",
    "asset_id" : "head486",
    "emp_details" : {
        "emp_assigned" : "Aarav Sharma",
        "emp_id" : "emp04",
        "emp_dept" : "Finance"
    },
    "purchase_price" : 1500,
    "warranty_status" : "2 years", 
    "asset_avail" : headphone_avail
}

office_furniture_details = {
    "asset_name" : "Office Furniture",
    "asset_id" : "office830",
    "emp_details" : {
        "emp_assigned" : "Neha Patel",
        "emp_id" : "emp05",
        "emp_dept" : "IT"
    },
    "purchase_price" : 40000,
    "warranty_status" : "4 years", 
    "asset_avail" : office_furniture_avail
}

print("========================================")
print("     Office Asset Management System     ")
print("========================================")

asset_list = {"Laptop","Projector","Keyboard","Headphone","Office Furniture"}
print("Asset's List : ", asset_list)
print()

asset_name = input("Enter the name of the asset which you want to track: ")
print()

if asset_name.lower() == "laptop" :
    if laptop_avail > 0 :
        for key,value in laptop_details.items():
            print(key,":",value)
    else :
        print("SORRY! Laptop is OUT OF STOCK.")

elif asset_name.lower() == "projector" :
    if projector_avail > 0 :
        for key,value in projector_details.items():
            print(key,":",value)
    else :
        print("SORRY! Projector is OUT OF STOCK.")

elif asset_name.lower() == "keyboard" :
    if keyboard_avail > 0 :
        for key,value in keyboard_details.items():
            print(key,":",value)
    else :
        print("SORRY! Keyboard is OUT OF STOCK.")

elif asset_name.lower() == "headphone" :
    if headphone_avail > 0 :
        for key,value in headphone_details.items():
            print(key,":",value)
    else :
        print("SORRY! Headphone is OUT OF STOCK.")

elif asset_name.lower() == "office furniture" :
    if office_furniture_avail > 0 :
        for key,value in office_furniture_details.items():
            print(key,":",value)
    else :
        print("SORRY! Office Furniture is OUT OF STOCK.")

else :
    print("Invalid Asset Name !!!")
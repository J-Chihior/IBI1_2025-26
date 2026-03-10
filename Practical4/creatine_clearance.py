# 1 store the value of a person's basic information: age, weight, gender and creatine"
# 2 check if input variables meet requirements
# 3 if valid, calculate CrCl
# 4 if femal: multiply by 0.85
# 5 print esult
# 6 if invalid, print the exact error
age = 25
weight = 120
gender = "male"
Cr = 80
if age >= 100:
    print ("Error:age should be less than 100")
elif weight <= 20 or weight>= 80 :
    print ("Error: weight should be between 20 and 80")
elif Cr <= 0 or Cr >= 100 :
    print(" Error: creation concentration should be between 0 and 100 ")
elif gender != "female" and gender != "male":
    print("Error: gender should be either male or female")
else:
    CrCl = ((140-age)* weight)/ (72* Cr) 
    if gender == "female" :
        CrCl = CrCl * 0.85
    print("Creatine clearance:", CrCl)
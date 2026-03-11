# 1 store the value of a person's basic information: age, weight, gender and creatine"
# 2 check if input variables meet requirements
# 3 if valid, calculate CrCl
# 4 if femal: multiply by 0.85
# 5 print esult
# 6 if invalid, print the exact error
age = int(input("please enter your age"))
weight = float(input("please enter your weight, in kg"))
gender = input("please enter your gender")
Cr = float (input("please enter your creation concentration, in µmol/l"))
error = False
if age >= 100:
    print ("Error:age should be less than 100")
    error = True
if weight <= 20 or weight>= 80 :
    print ("Error: weight should be between 20 and 80")
    error = True
if Cr <= 0 or Cr >= 100 :
    print("Error: creation concentration should be between 0 and 100 ")
    error = True
if gender != "female" and gender != "male":
    print("Error: gender should be either male or female")
    error = True
if error == False:
    CrCl = ((140-age)* weight)/ (72* Cr) 
    if gender == "female" :
        CrCl = CrCl * 0.85
    print("Creatine clearance:", CrCl)
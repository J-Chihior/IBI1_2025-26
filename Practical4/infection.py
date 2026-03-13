# 1 set initial infected number
# 2 set growth rate
# 3 set class size
# 4 set loops until everyone infected
# 5 print everyday's infected number
# 6 print the number of days taken to infect all
infected = 5 # assign the value of initial infected number
growth_rate = 0.4 # assign the value of growth rate
class_size = 91 # assign the value of class size
day = 1
while infected < class_size :
    print("Day",day,"infected number",infected)
    infected = infected + growth_rate * infected 
    day+=1
if infected >= 91:
    infected = 91
print("Day", day, ":", infected, "infected")
print ("All students infected after",day,"days")
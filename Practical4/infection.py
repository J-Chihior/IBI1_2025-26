# 1 set initial infected number
# 2 set growth rate
# 3 set class size
# 4 set loops until everyone infected
# 5 print everyday's infected number
# 6 print the number of days taken to infect all
infected = 5
growth_rate = 0.4
class_size = 91
day = 1
while infected < class_size :
    print("Day",day,"infected number",infected)
    infected = infected + growth_rate * infected
    day+=1
print("Day", day, ":", infected, "infected")
print ("All students infected after",day,"days")
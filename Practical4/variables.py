a=5.08 # assign the value of population for the year 2004
b=5.33 # assign the value of population for the year 2014
c=5.55 # assign the value of population for the year 2024
d=b-a # Calculate the change between 2004 and 2014
e=c-b # Calculate the change between 2014 and 2024
# Print the change from 2004 to 2014
print("change 2004-2014:", d)
# Print the change from 2014 to 2024
print("change 2014-2024:", e)
# Compare the two changes to determine the growth trend
if d<e:
    print("Growth is acelerating")
elif d>e:
    print("Growth is decelerating")
else:
    print("Growth rate is constant")
# d=0.25, e=0.21999999999999975
# d is larger than e
# The population growth appears to be declarating because the increase from 2014 to 2024 is smaller than that from 2014 to2024
X = True
Y = False
W = X or Y
print("W =", W)
# Truth table for W =X or Y
# X       Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False
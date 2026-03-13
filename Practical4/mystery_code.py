# What does this piece of code do?
# Answer: The code generates 11 random integers between 1 and 10, add them together ,and print the total sum

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint # draw a random number

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil #take the ceiling of a number

total_rand = 0
progress=0
while progress<=10: # draw 11 random numbers between 1 and 10
	progress+=1
	n = randint(1,10)
	total_rand+=n

print(total_rand)


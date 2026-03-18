#establish two dictionaries
Population_2020={"UK":66.7,"China":1426,"Italy":59.4,"Brazil":208.6,"USA":331.6}
Population_2024={"UK":69.2,"China":1410,"Italy":58.9,"Brazil":212.0,"USA":340.1}

#calculate the percentage change of each population
change={}
for country in Population_2020:
    percentage_change=(Population_2024[country]-Population_2020[country])/Population_2020[country]*100
    population_change=Population_2024[country]-Population_2020[country]
    print(f"{country}:{percentage_change:.2f}%")
    change[country]=population_change #wrong reason：forget to indent

#rank the population changes in descending order
sorted_change=sorted(change.items(),key=lambda x:x[1],reverse=True)
print("population change ranking:")
for country,value in sorted_change:
    print(f"{country}: {value:.1f}")

#identify the countries with the largest change in population
largest_increase = sorted_change[0]
largest_decrease = sorted_change[-1]
print("the largest increase country:",largest_increase)
print("the largest decrease country:",largest_decrease)

#draw bar chart shwing the population change for each country
import matplotlib.pyplot as plt
countries=list(change.keys())
values=list(change.values())
plt.bar(countries,values)
plt.ylabel("population change")
plt.title("Population Growth Rate")
plt.xlabel("countries")
plt.axhline(0, color='black', linewidth = 0.5)
plt.show()
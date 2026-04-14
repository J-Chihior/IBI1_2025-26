#import neccessary libraries
import numpy as np
import matplotlib . pyplot as plt
from matplotlib import cm

# add vaccinated person to the population
N=10000
β=0.3 
Ɣ=0.05

vaccinated_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]#add different rate of vaccinated using list

plt.figure (figsize =(6 ,4) , dpi =150)

for v in vaccinated_rate:
    vaccinated=int((N-1)*v)#change vaccinated to int in case of float
    Infected=1
    Susceptible=N-1-vaccinated
    Recovered=0


#create arrays for infected people
    Infected_list=[Infected]

#Recovered=[]is not true!
#loop over 1000time points
#calculate the ptobability of infetion
#pick susceptible individuals at random to become infected
#pick infected individuals at random to become recovered
#assign new values to the variables
#add new output to the arrays
    num_loop=1000
    for i in range(num_loop):
        infected_prob=β*Infected/N
        new_infected=np.random.choice([0,1],size=Susceptible,p=[1-infected_prob,infected_prob]).sum()
        new_recovered=np.random.choice([0,1],size=Infected,p=[1-Ɣ,Ɣ]).sum()
        Susceptible-=new_infected
        Recovered+=new_recovered
        Infected=Infected+new_infected-new_recovered
        Infected_list.append(Infected)
    plt.plot(Infected_list, label=f"{int(v*100)}% vaccinated")

plt.plot (vaccinated_rate,color=cm.viridis(30))
plt.xlabel("Time")
plt.ylabel("Infected")
plt.title("Effect of vaccination")
plt.legend()
plt.show()

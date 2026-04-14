#import neccessary libraries
import numpy as np
import matplotlib . pyplot as plt

# define the basic variables
N=10000 #total number of people in the population
Infected=1 
Susceptible=9999
Recovered=0
β=0.3 
Ɣ=0.05

#create arrays for each of variables
Infected_list=[Infected]
Susceptible_list=[Susceptible]
Recovered_list=[Recovered]

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
    Recovered_list.append(Recovered)
    Infected_list.append(Infected)
    Susceptible_list.append(Susceptible)

#plot the result
plt.figure (figsize =(6 ,4) , dpi =150)#it should be put in front
plt.plot(Susceptible_list,label="Susceptible")
plt.plot(Infected_list,label="Infected")
plt.plot(Recovered_list,label="Recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.title("SIR model")
plt.savefig("SIR_plot.png", dpi=150, bbox_inches="tight")
plt.show()# don't forget to show!




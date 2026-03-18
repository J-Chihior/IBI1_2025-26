#establish a list
a_list=[]
heart_rate=[72,60,126,85,90,59,76,131,88,121,64]
#count the number of patients
num_patients=len(heart_rate)
#calculate the mean heart rate of all patients
mean_rate=sum(heart_rate)/len(heart_rate)
print("the number of patients in the databaset:",num_patients)
print(f"the mean value of heart rate:{mean_rate:.2f}")

#create a dictionary
my_dict={}
Rate_category={"Low":"<60bpm","Normal":"60-120bpm","High":">120bpm"}

#category each heart rate and calculate the number of each category
Low=0
Normal=0
High=0
for rate in heart_rate:
    if rate < 60:
        Low+=1
    elif rate>=60 and rate<=120:
        Normal+=1
    else:
        High+=1
print("Low:",Low)
print("Normal:",Normal)
print("High:",High)
#compare the three numbers to identify the largest number of patients

#method 1-use dictionary
categories = {"Low": Low,"Normal": Normal,"High": High}
largest = max(categories, key=categories.get)
print("Largest category:", largest)
#method 2-use the if loop
largest=max(Low,Normal,High)
if largest==Low:
    print("Largest category:", "Low")
if largest==Normal:
    print("Largest category:", "Normal")
if largest==High:
    print("Largest category:", "High")

#draw pie chat of heart rate categories 
import matplotlib.pyplot as plt
labels="Low","normal","High"
sizes=[Low,Normal,High]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Heart Rate Categories")
plt.show()
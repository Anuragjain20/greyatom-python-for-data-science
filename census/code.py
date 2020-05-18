# --------------
# Importing header files
import numpy as np
import warnings


warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record),axis=0)
age=census[:,0]
max_age=max(age)
min_age=min(age)
age_mean=round(np.mean(age),2)
age_std=round(np.std(age),2)
race=census[:,2]
def race_s(rac,x):
    y=np.where(rac==x)
    return y

race_0=race_s(race,0)
race_1=race_s(race,1)
race_2=race_s(race,2)
race_3=race_s(race,3)
race_4=race_s(race,4)
len_0=len(race_0[0])
len_1=len(race_1[0])
len_2=len(race_2[0])
len_3=len(race_3[0])
len_4=len(race_4[0])
minor=min(len_0,len_1,len_2,len_3,len_4)
minority_race=3
l=age>60



e=census[:,6]
senior_citizens=age[l]
working_hours_sum=sum(e[l])
senior_citizens_len=len(senior_citizens)

avg_working_hours=round((working_hours_sum/senior_citizens_len),2)
a=census[:,1]
p=a>10
high=a[p]
k=a<=10
low=a[k]
inc=census[:,7]
avg_pay_high=round(np.mean(inc[p]),2)
avg_pay_low=round(np.mean(inc[k]),2)
print(avg_pay_high)
print(avg_pay_low)







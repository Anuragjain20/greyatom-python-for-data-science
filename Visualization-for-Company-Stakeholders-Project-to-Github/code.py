# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data["Loan_Status"].value_counts()

loan_status.plot(kind="bar")
#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(["Property_Area","Loan_Status"]).size().unstack()

property_and_loan.plot(kind='bar', stacked=False)



plt.xlabel('Property Area')
plt.ylabel('Loan Status')
#Changing the x-axis label


#Changing the y-axis label
plt.xticks(rotation=45)



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack()

education_and_loan.plot(kind="bar",stacked=True)
#Changing the x-axis label
plt.xlabel("Education Status")
plt.ylabel("Loan Status")

#Changing the y-axis label
plt.xticks(rotation=45)




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']


graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind="density",label="label='Not Graduate'")
#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot
fig ,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,10))
ax_1.scatter('ApplicantIncome',"LoanAmount")
ax_1.set_title("Applicant Income")
#Plotting scatter plot
ax_2.scatter('CoapplicantIncome',"LoanAmount")
ax_2.set_title("Coapplicant Income")
data["TotalIncome"]=data["CoapplicantIncome"]+data['ApplicantIncome']
ax_3.scatter('TotalIncome',"LoanAmount")
ax_3.set_title("Total Income")


#Setting the subplot axis title




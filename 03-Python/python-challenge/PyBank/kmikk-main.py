import os
import csv

bank_data = os.path.join("Resources", "budget_data.csv")

# In this challenge, you are tasked with creating a Python script for analyzing 
# the financial records of your company. You will give a set of financial data 
# called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
# composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company 
# has rather lax standards for accounting so the records are simple.)



#   Define needed lists
pandl = []
month = []
plchange = []   


#   Open and read file, skipping header row
with open(bank_data) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
#   Find needed data in file
    for row in csvreader:
        month.append(row[0])
        pandl.append(float(row[1]))


# Your task is to create a Python script that analyzes the records to calculate
# each of the following:


  # The total number of months included in the dataset
num_of_months = len(month)
  
  # The net total amount of "Profit/Losses" over the entire period
net_total = sum(pandl)

  # The average of the changes in "Profit/Losses" over the entire period
for i in range(1,len(pandl)):
    plchange.append(pandl[i] - pandl[i-1])
    average = round((sum(plchange)/len(plchange)),2)

  # The greatest increase in profits (date and amount) over the entire period
    maxpandl = max(plchange)
    maxmonth = str(month[plchange.index(max(plchange))])

  # The greatest decrease in losses (date and amount) over the entire period
    minpandl = min(plchange)
    minmonth = str(month[plchange.index(min(plchange))])


#   Print Results
analysis = "Financial Analysis \n----------------------------\nTotal Months: " + str(num_of_months) + "\nTotal: $" + str(net_total) + "\nAverage Change: $" + str(average) + "\nGreatest Increase in Profits: " + str(maxmonth) + " $" + str(maxpandl) + "\nGreatest Decrease in Profits: " + str(minmonth) + " $" + str(minpandl)

print(analysis)


#   Export to txt file

export = open('kmikk-analysis.txt', 'w')
export.write(analysis)
export.close()
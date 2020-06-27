# Set-up python environment
import os
import csv

# Identify location of data
# location = 'C:\Users\2250h\Documents\STUDY\UWA-Bootcamp\Homework\03-Python\python-challenge\PyBank\'
pybank = os.path.join('resources', 'budget_data.csv')
analysis = os.path.join('analysis', 'budget_analysis.txt')

#open file and create file reader
with open(pybank,newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

with open(pybank, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #defining and initializing variables
    totalMonths = 0
    totalRevenue = 0
    greatestProfit = 0
    greatestProfitDate = ""
    greatestLoss = 0
    greatestLossDate = ""

    #reading through each row in CSV,
    for row in csvreader:
        #add 1 to total month count
        totalMonths += 1
        #add value to net amount
        totalRevenue += int(row[1])
        
     

#output statements
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: " + str(totalRevenue))
print("Greatest Increase in Profits: " + greatestProfitDate + " ($" + str(greatestProfit) + ")")
print("Greatest Decrease in Profits: " + greatestLossDate + " ($" + str(greatestLoss) + ")")
print("----------------------------")


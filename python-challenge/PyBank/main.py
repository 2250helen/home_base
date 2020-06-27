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
        
        #if next row's revenue value is positive,
        if (int(row[1]) > 0):
            #compare it to the current greatest profit value, if greater,
            if (int(row[1]) > greatestProfit):
                #replace the greatest profit value and date
                greatestProfitDate = row[0]
                greatestProfit = int(row[1])
        #if next row's revenue value is negative,
        if (int(row[1]) < 0):
            #compare it to the current greatest loss value, if less,
            if (int(row[1]) < greatestLoss):
                #replace the greatest loss value and date
                greatestLossDate = row[0]
                greatestLoss = int(row[1])

#output statements
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: " + str(totalRevenue))
print("Greatest Increase in Profits: " + greatestProfitDate + " ($" + str(greatestProfit) + ")")
print("Greatest Decrease in Profits: " + greatestLossDate + " ($" + str(greatestLoss) + ")")
print("----------------------------")


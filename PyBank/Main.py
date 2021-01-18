# Import OS and CSV
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Create new variables
Total_Months = 0
Net_Profit_Loss = 0
Running_Profit_Loss = []
Avg_Proft_Loss_Change = 0
Greatest_Increase = []
Greatest_Decrease = []
Previous_Row = 0

# Read Budget_Data CSV File
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    # budget = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csv_header = next(budget_data)

    # Start loop for month count
    for row in budget_data:
        Total_Months += 1

        # Calculate Profit/Loss for Entire Period
        Net_Profit_Loss = int(row[1]) + Net_Profit_Loss
        Running_Profit_Loss = Avg_Proft_Loss_Change
        Running_Profit_Loss = int(row[1]) - Previous_Row   
        Previous_Row = int(row[1])     
       #Avg_Proft_Loss_Change = (sum(Running_Profit_Loss))/(len(Running_Profit_Loss))

        # Calculate greatest increase in profits (include date and amount)
        
        # Calculate greatest decrease in profits (include date and amount)

print(Total_Months)
print(Net_Profit_Loss)
print(Avg_Proft_Loss_Change)
print(Greatest_Increase)
print(Greatest_Decrease)



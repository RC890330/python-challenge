import os
import csv
import sys

# Setting path to collect data from the Resources folder
pwd = os.getcwd()
cwd = os.path.abspath(__file__)
dir_name = os.path.dirname(cwd)
csvpath = os.path.join(dir_name, "Resources", "budget_data.csv")
outputpath=os.path.join(dir_name,"Analysis","PyBank_analysis.txt")

# Define variable #
totalrow = 0
total = 0
previous = 1088983
totalchange = 0
avgchange = 0

# Setting list for change which will later store the change in profit amount
Change = []

# Setting variables for max and min for condition code in line 51 to 58
max = 0 
min = 0

# Opening the csv file #
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\n')

    # Skipping the first row that contains the heading 
    next(csvreader)
    
    # Count total number of rows in the csv file #
    for row in csvreader:
        
        # splitting the list (row)
        data = row[0].split(",")
        
        # net total amount of "Profit/Losses" over the entire period
        date = data[0]
        profit = int(data[1])
        totalrow += 1
        total += profit
        
        # Addition of the changes in Profit/Losses over the entire time
        Change.append(profit-previous)
        totalchange += (profit-previous)
        
        # Setting the current profit as previous profit
        previous = profit

        # The greatest increase in profits (date and amount) over the entire period
        for value in Change:
            if (max < value):
                max = value
                maxD = data[0]
        
        # Condition to find the greatest decrease in profits (date and amount) over the entire period 
            if (min > value):
                min = value
                minD = data[0]
        
    
    # Average of those changes
    avgchange = totalchange/(totalrow-1)

# Output to the terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalrow)}")
print(f"Total: ${str(total)}")
print(f"Average change: ${round(avgchange, 2)}")
print(f"Greatest Increase in Profits: {maxD} ({max})")
print(f"Greatest Decrease in Profits: {minD} ({min})\n")

# opening the path to where the txt file is located, using 'w' function to write into the file
with open(outputpath, 'w') as f:
          # Basically writing the output of the terminal into the txt file
          f.write("Financial Analysis\n")
          f.write("----------------------------\n")
          f.write(f"Total Months: {str(totalrow)}\n")
          f.write(f"Total: ${str(total)}\n")
          f.write(f"Average change: ${round(avgchange, 2)}\n")
          f.write(f"Greatest Increase in Profits: {maxD} ({max})\n")
          f.write(f"Greatest Decrease in Profits: {minD} ({min})\n")
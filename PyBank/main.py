import os
import csv

#set path
budget_data = os.path.join("budget_data.csv")

#set lists
#calculating the total months of data
total_months = 0
#overall profit or loss
total_prof_loss = 0

#to calculate change in data
change = 0
value = 0

#from data
months = []
profit = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read data after first row
    header = next(csvreader)
 
    for row in csvreader:
        months.append(row[0])

# The total number of months included in the dataset
        total_months = len(months)

# The net total amount of "Profit/Losses" over the entire period
        change = int(row[1]) - value
        profit.append(change)
        value = int(row[1])

        total_prof_loss = total_prof_loss + int(row[1])


# The average of the changes in "Profit/Losses" over the entire period

    average_change = sum(profit)/len(profit)


# The greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(profit)
    increase = profit.index(greatest_increase)
    increase_date = months[increase]

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profit)
    decrease = profit.index(greatest_decrease)
    decrease_date = months[decrease]



#Display findings
print("Financial Analysis")
print("------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_prof_loss)}")
print(f"Average change: ${str(round(average_change))}")
print(f"Greatest Increase in Profits: {increase_date} ${str(greatest_increase)}")
print(f"Greatesr Decrease in Profits: {decrease_date} ${str(greatest_decrease)}")
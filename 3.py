import csv
import os

budget_data_path = os.path.join("Pybank", "Resources", "budget_data.csv")

total_months = 0
total_profit_losses = 0
profits_losses = []
months = []
changes = []

try:
    with open(budget_data_path, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        # Read the header row
        header = next(csvreader)
        
        # Read each row of data after the header
        for row in csvreader:
            if len(row) < 2:
                continue
            
            # month and profit/loss from the row
            month = row[0]
            profit_loss = row[1]
            
        
if profit_loss == '' or profit_loss == 'Profit/Losses':
    continue
        
            profit_loss = int(profit_loss)
            
            # Add the month and profit/loss to their lists
            months.append(month)
            profits_losses.append(profit_loss)
            
            total_months += 1
            total_profit_losses += profit_loss
            
            # Calculate the changes in "Profit/Losses" between months
    if total_months > 1:
        change = profit_loss - profits_losses[-2]
        changes.append(change)
        
        #average change
if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0
        
        # Find the greatest increase and decrease in profits
    if changes:
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
            
        greatest_increase_month = months[changes.index(greatest_increase) + 1]
        greatest_decrease_month = months[changes.index(greatest_decrease) + 1]
     else:
        greatest_increase = 0
        greatest_decrease = 0
        greatest_increase_month = None
        greatest_decrease_month = None
        
        # Print the results in the desired format
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${total_profit_losses}")
        print(f"Average Change: ${average_change:.2f}")
        if greatest_increase_month is not None:
            print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
        if greatest_decrease_month is not None:
            print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

except FileNotFoundError:
    print(f"The file at path {budget_data_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

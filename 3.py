import os
import csv
csv_path = 'PyBank/Resources/budget_data.csv'

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")

    for row in csvreader:
        print(row)
Total_months = 0
total_profit_losses = 0

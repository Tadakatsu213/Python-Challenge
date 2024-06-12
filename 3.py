import csv
import os

budget_data = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

csv_header = next(csv_file)
print(f"Header: {csv_header}")

Total_months = 0
total_profit_losses = 0




import csv
import os
budget_data = os.path.join('..','Resources','budget_data.csv')

with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csv_reader)
    print(csv_header)

    total_months = []
    total_profit = []
    date =[]
    monthly_profit_change =[]
    
    
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        months_count = len((total_months))
        # find monthly change in profit
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        

    print(sum(monthly_profit_change)/len(monthly_profit_change))


    print(months_count)  
    print(sum(total_profit))



    
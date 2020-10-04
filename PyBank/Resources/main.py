
import csv
import os
budget_data = os.path.join('..','Resources','budget_data.csv')

#add lists
totalmonths = []
netprofit = []
profitchange = []

# Open and read csv file
with open("budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #for lope 
    for row in csvreader:
        totalmonths.append(row[0])
        netprofit.append(int(row[1]))
        
    for i in range(len(netprofit)-1):
        profitchange.append(netprofit[i+1]-netprofit[i])

# max and min values
increase = max(profitchange)
decrease = min(profitchange)

monthlyincrease = profitchange.index(max(profitchange))+1
monthlydecrease = profitchange.index(min(profitchange))+1

# print results
print("Financial Analysis")
print("-------------------")
print(f"Total Months:{len(totalmonths)}")
print(f"Total: ${sum(netprofit)}")
print(f"Average Change:{round(sum(profitchange)/len(profitchange),2)}")
print(f"Greatest Increase in Profits: {totalmonths[monthlyincrease]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {totalmonths[monthlydecrease]} (${(str(decrease))})")

# export text file 
output = "output.txt"
with open("output","w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("--------------------")
    new.write("\n")
    new.write(f"Total Months:{len(totalmonths)}")
    new.write("\n")
    new.write(f"Total: ${sum(netprofit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {totalmonths[monthlyincrease]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {totalmonths[monthlydecrease]} (${(str(increase))})")

    
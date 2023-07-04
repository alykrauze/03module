import csv
import os

csvpath = os.path.join("..","Resources", "budget_data.csv")
total_months = 0
total_profitloss = 0
profit_loss = []
previous_profit_loss = 0
month_of_change = []
profit_loss_change = 0
greatest_decrease = ["", 100000000]
greatest_increase = ["", 0]
change_list = []
profit_loss_average = 0


with open ("Resources/budget_data.csv", "r") as csv_file:
    csv_dict = csv.DictReader(csv_file)

    for row in csv_dict:

        #Count the total of months
        total_months += 1

        #Calculate the total revenue over the entire period
        total_profitloss = total_profitloss + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        profit_loss_change = float(row["Profit/Losses"])- previous_profit_loss
        previous_profit_loss = float(row["Profit/Losses"])
        change_list = change_list + [profit_loss_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        #The greatest increase in revenue (date and amount) over the entire period
        if profit_loss_change>greatest_increase[1]:
            greatest_increase[1]= profit_loss_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if profit_loss_change<greatest_decrease[1]:
            greatest_decrease[1]= profit_loss_change
            greatest_decrease[0] = row['Date']
    profit_loss_average = sum(change_list)/len(change_list)

print(total_months)
print(total_profitloss)
print(greatest_increase)
print(greatest_decrease)
print(profit_loss_average)


"""

for profit_loss in profit_losses: 
    total += profit_loss
    profit_change = profit_loss - previous_revenue
    previous_revenue = float(profit_loss)
    average_change = average_change + profit_change
    float_value = float(profit_loss)
    if float_value > max_value:
        max_value = float_value
    if float_value < min_value:
        min_value = float_value
    avergae = sum(average_change)/len(average_change)

months = len(monthsvalue)
print("Number of Months", months)
print("Total Profit/Loss", total)
print("Average",total/months)
print(max_value)
print(min_value)
print(average)
"""

"""""
    for values in csv_dict:
        print(values)
        monthsvalue.append(values["Date"])
        profit_losses.append(int(values["Profit/Losses"]))
    """
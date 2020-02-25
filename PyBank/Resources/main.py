# import libraries
import os
import csv

# define path
csvpath = os.path.join('budget_data.csv')

# initialize variables; generate empty list
countM = 0
sumPnL = 0
row = [1]
pl=[]

# open csv contents and run program to extract data into list
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header =next(csvreader)
    rows =[[row[0], int(row[1])] for row in csvreader]

for row in rows:
        date= row[0]
        pl.append(row[1])
  
# count months with for loop
for row in rows:
    countM = countM + 1
    sumPnL += int(row[1])
# sum values with for loop and use len to get total value count for average
for row in rows:
    avgpl = sumPnL/len(row[0])
    if row[1] == max(pl):
        q4 = f"{row[0]} {row[1]}"
    if row[1] == min(pl):
        q5 = f"{row[0]} {row[1]}"
     

print(f"Financial Analysis"
    f"-----------------------------"
    f"total months:  {countM}"
    f"total:  {sumPnL}"
    f"Average Change:  {avgpl}"
    f"Greatest Increase in Profits:   {q4}"
    f"Greatest Decrease in Profits:  {q5}")
Financial_Analysis = open("Financial_Analysis.txt","w")
Financial_Analysis.write(f"Financial Analysis\n Financial Analysis \n ----------------------------- \n total months:  {countM} \n total:  {sumPnL} \n Average Change:  {avgpl} \n Greatest Increase in Profits:   {q4} \n Greatest Decrease in Profits:  {q5} ")

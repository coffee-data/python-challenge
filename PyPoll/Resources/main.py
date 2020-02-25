# import libraries
import os
import csv

# define path
csvpath = ('election_data.csv')

# initialize variables
countV = 0 
Khanvotes = 0 
Correyvotes = 0
Livotes = 0
Tooleyvotes = 0
pKhan = 0
pCorrey = 0
pLi = 0
pTooley = 0

# open path and load into variable csvreader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # set header
    header =next(csvreader)

    # populate variable rows with list of csv data
    rows =[[row[0], row[1], row[2]] for row in csvreader]

# for loop for counting votes
for row in rows:
    countV = countV + 1


candidates = []

# count per candidate
for x in rows:
    if x[2] not in candidates:
        candidates.append(x[2])

    if x[2] == 'Khan':
        Khanvotes += 1

    if x[2] == 'Correy':
        Correyvotes += 1

    if x[2] == 'Li':
        Livotes += 1
    
    if x[2] == "O'Tooley":
        Tooleyvotes += 1

# set percentage of total votes
pKhan = (Khanvotes / countV)*100
pCorrey = (Correyvotes / countV)*100
pLi = (Livotes / countV)*100
pTooley = (Tooleyvotes / countV)*100

# determine winner based on max
winner = max(Khanvotes,Correyvotes,Livotes,Tooleyvotes)
if winner == Khanvotes:
    winnername = 'Khan'
if winner == Correyvotes: 
    winnername = 'Correy'
if winner == Livotes:
    winnername = 'Li'
if winner == Tooleyvotes: 
    winnername = "O'Tooley"

print(f' Election Results \n'
    f'------------------------- \n'
    f'Total Votes:{countV} \n'
    f'------------------------- \n'
    f'Khan: {round(pKhan)}% ({Khanvotes}) \n'
    f'Correy: {round(pCorrey)}% ({Correyvotes}) \n'
    f'Li: {round(pLi)}% ({Livotes}) \n'
    f'OTooley: {round(pTooley)}% ({Tooleyvotes}) \n'
    f'------------------------- \n'
    f'Winner: {winnername}')

resultsdoc = open('Election_Results.txt', 'w')
resultsdoc.write(f' Election Results \n ------------------------- \n Total Votes:{countV} \n ------------------------- \n Khan: {round(pKhan)}% ({Khanvotes}) \n Correy: {round(pCorrey)}% ({Correyvotes}) \n Li: {round(pLi)}% ({Livotes}) \n OTooley: {round(pTooley)}% ({Tooleyvotes}) \n ------------------------- \n Winner: {winnername}')
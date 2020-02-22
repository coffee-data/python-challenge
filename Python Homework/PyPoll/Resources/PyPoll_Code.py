import os
#imoort csv library
import csv
csvpath = ('election_data.csv')
#initialize countv to 0
countv = 0
#open path as variable
countCorrey = 0
countKhan = 0
countLi = 0
countOTooley = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #next is csv which takes first line
    header = next(csvreader)
    rows =[[row[0], row[1], row[2]] for row in csvreader]
for row in rows:
    countv = countv+1
print(countv)

candidates = []

for row in rows:
    if row[2] not in candidates:
        candidates.append(row[2])
    if row[2] == "Khan":
        countKhan += 1
    if row[2] == "Correy":
        countCorrey += 1
    if row[2] == "Li":
        countLi += 1
    if row[2] == "O'Tooley":
        countOTooley += 1

pCorrey = (countCorrey / countv)*100
pKhan = (countKhan / countv)*100
pLi = (countLi / countv)*100
pOTooley = (countOTooley / countv)*100

print(f'Correy = {countCorrey} Khan = {countKhan} Li ={countLi} Li ={countLi}')
print(candidates)
print(f'Correy = {pCorrey} Khan = {pKhan} Li = {pLi} OTooley = {pOTooley}%')

winner = max(pCorrey,pKhan,pLi,pOTooley)
if winner == pCorrey:
    winnername = "Correy"
if winner == pKhan:
    winnername = "Khan"
if winner == pLi:
    winnername = "Li"
if winner == pOTooley:
    winnername = "O'Tooley"

print(f'{winnername} @ {winner}')

resultsdoc = open("Election_Results.txt", "w")

results = [("Correy", pCorrey, countCorrey),("Khan", pKhan, countKhan),("Khan", pLi, countLi),("O'Tooley", pOTooley, countOTooley)]
for entry in results:
    print(results)

# reference code DELETE
grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]

#left off needing to create a series to solve refrencing the winner.
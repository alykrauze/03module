import csv
import os
from collections import Counter

csvpath = os.path.join("..","Resources", "election_data.csv")

total_votes = 0
Candidates = {}
percent_votes_won = 0
total_number_votes = 0 
winner = ""
Candidate_Name = []
Candidate_Names = []
Name = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open ("Resources/election_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1 
        Candidate_Name = row[2]
        Candidate_Names.append(Candidate_Name)

row = Candidate_Names
unique_names = set(row)
count_names = Counter(row)

print(total_votes)

for value in unique_names:
    count = count_names[value]
    percent = (count)/(total_votes) * 100
    print(f"Name: {value}, Total Votes: {count}, Percent: {percent}")
    
    if (count > winning_count) and (percent > winning_percentage):
        winning_count = count 
        winning_candidate = value
        winning_percentage = percent    
        
print(f"Winner: {winning_candidate}")



    
   



        





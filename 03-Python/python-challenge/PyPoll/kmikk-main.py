#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#   The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to 
#   create a Python script that analyzes the votes and calculates each of the following:
import os
import csv


election_data = os.path.join("Resources", "election_data.csv")




#   Define needed lists
votes = {}
total_votes = []
results = ""
most_votes = 0

#   Open and read file
with open(election_data) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
#   Find needed data in file
    for row in csvreader:
        total_votes.append(row[0])
        candidate = row[2]
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1
    
#   Find needed data 

#  * The total number of votes cast
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
for c in votes:
    num_votes = votes[c]
    percentage = round(100 * (votes[c] / len(total_votes)))
    line = (str(c) + ": " + str(percentage) + "% (" + str(num_votes) + ")\n")
    results += line


#  * The winner of the election based on popular vote.

for key, value in votes.items():
    if votes[key] > most_votes:
        most_votes = votes[key]
        winner = key


#   Final Output
        
election_results = "Election Results\n-------------------------\nTotal Votes: " + str(len(total_votes)) + "\n-------------------------\n" + results + "-------------------------\nWinner: " + winner + "\n-------------------------"


print(election_results)


export = open('kmikk-election_results.txt', 'w')
export.write(election_results)
export.close()


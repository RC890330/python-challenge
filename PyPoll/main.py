import os
import csv
import sys

# Setting path to collect data from Resources 
pwd = os.getcwd()
cwd = os.path.abspath(__file__)
dir_name = os.path.dirname(cwd)
csvpath = os.path.join(dir_name, "Resources", "election_data.csv")
outputpath=os.path.join(dir_name,"Analysis","PyPoll_analysis.txt")

# Setting variables 
total_votes = 0
candidate_votes = {}

# Total number of votes cast
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # This code skips a row (skipping the heading)
    next(csvreader)
    
    # For loop for the all the following rows
    for row in csvreader:
        
        # Calculate for total number of votes cast
        total_votes += 1
        
        
        # Define where each data is located in the list 
        name = row[2]
        
        if name in candidate_votes:
            candidate_votes[name] += 1
        else:
            candidate_votes[name] = 1

winner = max(candidate_votes, key=candidate_votes.get)


#Output to the terminal
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = round(((votes/total_votes) * 100), 3)
    print(f"{candidate}: {percentage}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------\n")

# Output to the txt
with open(outputpath, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = round(((votes/total_votes) * 100), 3)
        f.write(f"{candidate}: {percentage}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------")
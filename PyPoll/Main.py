# Import OS and CSV
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Create new variables
Total_Votes = 0
Candidate_List = []
Vote_Percentages = []
Votes_By_Candidate = []
Winner = 0

# Read Election_Data CSV File
with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    csv_header = next(election_data)

    # Start for the for loop for vote count
    for row in election_data:
        Total_Votes += 1

        # Create candidate list, votes by candidate and percentages
        if row[2] not in Candidate_List:
            Candidate_List.append(row[2])
            Votes_By_Candidate.append(0)
            Vote_Percentages.append(0)
        #for i, candidate in enumerate(Candidate_List)
            #if candidate == row[2]
            #Votes_By_Candidate[i] +=1


print(Total_Votes)
print(Candidate_List)
print(Vote_Percentages)
print(Votes_By_Candidate)
print(Winner)
    

import os
import csv

csvpath = os.path.join('.','Resources','election_data.csv')

total_Votes = 0
candidates = []
vote_Count = []
winner_VoteCount = 0
# Open and read csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
 
 #Loop the file
    for row in csvreader:
        total_Votes += 1

        if(row[2] not in candidates):
            candidates.append(row[2])
            vote_Count.append(0)
        
        candidate_Index = candidates.index(row[2])
        vote_Count[candidate_Index] += 1

    #Printing output
    print(f"\nElection Results\n------------")
    print(f"Total votes: {total_Votes}")
    print("------------------------------")
    
    for i in range(len(candidates)):
        vote_Percent = round((vote_Count[i]/total_Votes)*100,2)
        print(f"{candidates[i]}: {vote_Percent}% ({vote_Count[i]})")
        if (winner_VoteCount<vote_Count[i]):
            winner_VoteCount = vote_Count[i]
            winner = candidates[i]
    
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")


#export text file   
file = open('output.txt','w')
file.write("Election Results")
file.write("\n-------------------------------")
file.write("\nTotal votes:" + str(total_Votes))
file.write("\n--------------------------------")
    
for i in range(len(candidates)):
    vote_Percent = round((vote_Count[i]/total_Votes)*100,2)
    file.write("\n" + str(candidates[i]) +" : " + str(vote_Percent) 
                + "% ("+ str(vote_Count[i]) + ")")
file.write("\n----------------------------")
file.write("\nWinner: " + str(winner))
file.write("\n-----------------------------")

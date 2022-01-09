# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
election_results = os.path.join ('Election-analysis','Resources','election_results.csv')
# Assign a variable to save the file to a path
election_write = os.path.join ('Election-analysis','Resources', 'election_analysis.txt')
#  Initialize the total vote counter
total_votes = 0   
# Declare a new list to store the Candidate name
candidate_options =[]
# Open the election results and read the file.
# Declare empty dictionary to store votes for each candidate
candidate_votes ={}
# Tracking the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(election_results) as election_data:
    # Read the file object with the reader function
    csv_reader = csv.reader(election_data, delimiter =',')
       
    # Read the header row
    headers = next(csv_reader)
    # To print headers use - print (headers)
     #  print each row in the CSV file
    for row in csv_reader:

        # Add the total Vote Count
        total_votes += 1

        # get the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate then add it to list cand-options
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
                 
        # Increament candidate vote count
        candidate_votes[candidate_name] += 1

    with open(election_write, "w") as txt_file:
        election_results =(
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------------\n")
        print (election_results, end="")
        txt_file.write(election_results)
        # outfile = open(election_write, "w")
        # outfile.write ('Election Results\n-------------------------------------\nTotal Votes: 369,711\n-----------------------------------------------------\n')
            
    
        # Iterate through Candidate list
        for candidate_name in candidate_votes:
            
            # retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes
            Vote_percentage = float (votes) / float(total_votes)*100 

            # print the candidate name and percentage of votes
            print (f'{candidate_name}: received {Vote_percentage:.1f}% of the vote.')

            # print out each candidate's name, vote count, and percentage of votes to terminal
            candidate_results = (f'{candidate_name} : {Vote_percentage:.1f}% ({votes:,})\n')
            print (candidate_results)
            txt_file.write(candidate_results)


            # Winning Candidate and Winning Count Tracker        
            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if (votes > winning_count) and (Vote_percentage > winning_percentage):
                # if the above condition is then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = Vote_percentage
                # set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        #   Print the winning candidate's results to the terminal
        Winning_candidate_summary = (
            f'.....................................\n'
            f'Winner:{winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'--------------------------------------\n')
        print (Winning_candidate_summary)
        # Save the winning candidate's name to the text file
        txt_file.write (Winning_candidate_summary)

        
#     print (f'The winning candidate of the election is {winning_candidate} with {winning_count} votes and {winning_percentage:.1f}%')   

     
# # Print the total votes
# print (f'Total votes casted = {total_votes}')
# # print the candidate list
# print(f'The candidates in election are {candidate_options}')
# #  Print each candidate votes
# print(f'The list of candidates and their vote is {candidate_votes}')

    

#     # CSV reader specifies delimiter and variable that holds contents


# TO WRITE A FILE TO A DIRECTORY ON YOUR COMPUTER
# # Create a filename variable to a direct or indirect path to the file.

# # # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(election_write, "w")
# # # Use the open statement to open the file as a text file.
# # outfile = open('election_analysis.txt', "w")
# # # Write some data to the file.
# outfile.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson\n")


# # # Close the file
# outfile.close()
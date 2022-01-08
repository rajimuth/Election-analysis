# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
election_results = os.path.join ('Election-analysis','Resources','election_results.csv')
# Assign a variable to save the file to a path
election_write = os.path.join ('Election-analysis','Resources', 'election_analysis.txt')
# Open the election results and read the file.
with open(election_results) as election_data:
    # Read the file object with the reader function
    csv_reader = csv.reader(election_data, delimiter =',')
        #  print each row in the CSV file
    # for row in csv_reader:
    #     print(row)
    headers = next(csv_reader)
    print (headers)

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
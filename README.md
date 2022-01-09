# Election-analysis
## Election Audit Overview:
Coloroda Board of elections employee needs help to complete the election audit of the tabulated results from a local congressional election. The data has information on Ballot ID, County in which the vote was casted and the candidate name who got the vote. Though the analysis can be done with excel, they want to automate the process in the future for other election analysis using Python.
### Goals of the Election audit Analysis:
The goal of the election results analysis is to
1) Calculate the total number of votes casted for all candidates in all counties
2) Calculate the voter turnout for each county
3) Calculate the percentage of votes from each county out of the total count
4) Identify the county with highest turnout
5) Calculate the total number of votes for each candidates 
6) Calculate the percentage of votes for each candidate
7) Identify and declare the winning candidate of the election based on popular vote count 
### Resources used:
Data was obtained from election_results.csv file
### Overview of Analysis Methods and Election Audit Results:
##### Before starting the analysis a variable was assigned to have the path of the csv file data in which the analysis needs to be performed. In our case the file to be analyzed was election_results.csv. The variable to hold this file was election_results.The data in the CSV file was opened using the with open (variable name)  syntax and read using csv.reader
##### The results are to be written in election_analysis.txt.The variable assigned to hold the path of this file in which analyzed results need to be written is election_write. After each analysis the results were saved to the text file (election_results.txt) using the with open syntax (variable name,write mode).
The methods and results for each goal of analysis is outline below.
#### Goal 1: Calculate Total number of votes
- A variable (total_votes) was initialized to store the total number of votes
- FOR loop was used to loop through each row of the csv file
- Each row in the csv file has data for each vote
- The total vote was counted with every cycle of the loop and stored in the variable total_votes
##### The total vote is calculated to be 369,711 
#### Goal: 2) Calculate the voter turnout for each county
#### Goal: 3) Calculate the percentage of votes from each county out of the total count
- To calculate this, we first need to know how many counties are in the data
- A variable (county_list) was initialized to store the list that has names of all counties in the list
- As the FOr loop run through each row, its going to add (append) the county name (row[1]: which is in the second index of the row) to the list.
- If not in conditional statement was added to check if the county name is already in the list and not add  if the name is in the list. This avoids repetetion of county names
- Next, we want to calculate the total vote count for each county as store it.
- To store this data of county name (from the list - county_list) and the vote turnover that will be calculated, we intitalize a county votes dictionary (county_votes)
- The key in this dictionary is the county_name and the vlaue for each key will be cty_votes
- county_votes[county_name] which will hold the value of vote count for that county_name is intialized to zero
- A vote is added to the county's vote count for each loop
- cty_votes then retrieve/get  the county vote count from county_votes(county_name)
- The perecntage of votes for that county (stores in variable county_percentage) is calculated from county votes (cty_votes) and total votes (total_votes)
- The result that holds the information of county_name, county_percentage and cty_votes is assigned to a variable county_results. It is printed and written to the election_analysis.txt using the txt_file.write syntax
/*txt_file.write(county_results)/*
##### The result of this analysis is shown below:
County Votes:
Jefferson: 10.5%  (38,855)
Denver: 82.8%  (306,055)
Arapahoe: 6.7%  (24,801)
#### Goal: 4) Identify the county with highest turnout
- Two variables Votes_turnout and large_turnout_county were intitalized
- Votes_turnout is initialized to zero and large_turnout_county is initialized with an empty string
- As cty_votes (total votes for each county) is calculated, an IF conditional statement was added to see if the cty_votes is greater than Votes_turnout (which is 0 for the first vote count alazyled)
- If it is greater then, the Votes_turnout variable now holds the vote count for that county (in our case it is cty_votes for jefferson which is 38,855) and the Large_turnout_county will hold the name of that county (Jefferson)
- When the total vote count for the next county (in out case the second county in the list is Denver)comes in, the cty_votes is checked if it is greater than the Votes_turnout (it has the value for the Jefferson county vote -38,855 count now)
- If it is greater, then Votes_turnout will now hold the value of that cty_votes (Denver)
- The cycle will thus loop throught the list to determine the county with large vote turnover
##### The result of this analysis shows:
 Largest County Turnout:Denver
 #### Goal: 5) Calculate the total number of votes for each candidates #### Goal: 6) Calculate the percentage of votes for each candidate
 To calculate this, we first need to know how many candidates are in the data
- A variable (candidate_options) was initialized to store the list that has names of all candidates in the list
- As the FOR loop run through each row, its going to add (append) the candidate name (row[2]: which is in the third index of the row) to the list.
- If not in conditional statement was added to check if the candidate name is already in the list and not add  if the name is in the list. This avoids repetetion of candidate names
- Next, we want to calculate the total vote count for each candidate.
- To store this data of candidate name (from the list - candidate_options) and the vote turnover that will be calculated, we intitalize a candidate votes dictionary (candidate_votes)
- The key in this dictionary is the candidate_name and the vlaue for each key will be candidate_votes
- vandidate_votes[candidate_name] which will hold the value of vote count for that county_name is intialized to zero
- A vote is added to the candidate's vote count for each loop
- votes then retrieve/get  the county vote count from county_votes(county_name)
- The perecntage of votes for that county (stores in variable voye_percentage) is calculated from candidate's votes (votes) and total votes (total_votes)
- The result that holds the information of candidate_name, vote_percentage and votes is assigned to a variable candidate_results. It is printed and written to the election_analysis.txt using the txt_file.write syntax
/*txt_file.write(candidate_results)/*
##### The result of this analysis is shown below:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
#### Goal: 7) Identify and declare the winning candidate of the election based on popular vote count 
Three variables winning_count, winning_candidate and winning_percentage were intitalized
- winning_count and winning percentage is initialized to zero and winning_candidate is initialized with an empty string
- As candidate_votesvotes and votes_percentage (total votes and percentage for each candidate) is calculated, an IF conditional statement was added to see if the votes and votes_percentage is greater than winning_count and winning_percentage (which is 0 for the first vote count analyzed)
- If it is greater, then the winning_votes and winning_percentage variable now holds the votes and votes_percentage for that candidate (in our case it is votes for Charles Casper Stockham which is 85,213 and 23%) and the winning_candidate will hold the name of that candidate(Charles Casper Stockham)
- When the total vote count for the next candidate (in our case the second candidate in the list is Diana DeGette)comes in, the votes and votes_percentage is checked if it is greater than the winning_votes and winning_percentage (it has the value for the Charles Casper Stockham  votecount 85,213 and 23%  now)
- If it is greater, then Votes_turnout will now hold the value of that candidate (Diana DeGette)
- The cycle will thus loop throught the list to determine the candidate with te winning vote count and winning percentage
##### The result of this analysis is shown below:
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

## Election Audit Summary
<<<<<<< HEAD
### The tabulated results from a local coloroado congressional election was analyzed to calculate the total votes, vote turn over and percentage for each counties where the elction was held and the total vote and percentage of votes received by each candidate. This result helped the election commission declare the winning candidate and the winning vote count and winning percentage for that candidate.
### Our primary plan of using this python code to be applied for any election result analysis can be achieved by changing the path of the file to be loaded/read and changing the path of the written text file. More FOR loops can be added if the row as had additional information like state/district name, party name .
#### example 1:  if it is a senate election with additional data for each state in row[3], then the state name, total vote count and percentage in each state can be calcuated by adding the below script
state_list =[]
state_votes ={}
large_turnout_state= 0
large_stateturnout_votes =0 
state_name =row[3]
if state_name not in state_list:
state_list.append(state_name)
state_votes[state_name] = 0
state_votes[state_name] += 1
for state_name in state_votes:
stvotes = state_votes.get(state_name)
stpercentage = float(stvotes)/float(total_votes)*100
state_results =(f"{state_name}: {stpercentage:.1f}% ({stvotes}))
#### example 2: If the election data also has inforamtion on the party names (Democratic/Republic/Independent),
then the scipt can be added to declare the winning party as well
party_list =[]
party_votes ={}
winning_party =""
vote_winning_party = 0
percentage_winning_party = 0
party_name = row[4] # assumiong the information is in column 5
if party_name not in party_list:
party_list.append(party_name)
party_votes[party_name] = 0
party_votes[party_name] += 1
for party_name in party_votes:
ptyvotes = party_votes.get(party_name)
ptypercentage = float(ptyvotes)/float(total_votes)*100
party_results =(f"{party_name}: {ptypercentage:.1f}% ({ptyvotes}))
=======
The tabulated results from a local coloroado congressional election was analyzed to calculate the total votes, vote turn over and percentage for each counties where the elction was held and the total vote and percentage of votes received by each candidate. This result helped the election commission declare the winning candidate and the winning vote count and winning percentage for that candidate.
Our primary plan of using this python code to be applied for any election result analysis can be achieved by changing the path of the file to be loaded/read and changing the path of the written text file. More FOR loops can be added if the row as had additional information like state/district name, party name .
#### Example 1:  
If it is a senate election with additional data for each state in row[3], then the state name, total vote count and percentage in each state can be calcuated by adding the below script
###### state_list =[]
###### state_votes ={}
###### large_turnout_state= 0
###### large_stateturnout_votes =0 
###### state_name =row[3]
###### if state_name not in state_list:
###### state_list.append(state_name)
###### state_votes[state_name] = 0
###### state_votes[state_name] += 1
###### for state_name in state_votes:
###### stvotes = state_votes.get(state_name)
###### stpercentage = float(stvotes)/float(total_votes)*100
###### state_results =(f"{state_name}: {stpercentage:.1f}% ({stvotes}))
#### Example 2: 
If the election data also has inforamtion on the party names (Democratic/Republic/Independent),
then the scipt can be added to declare the winning party as well
###### party_list =[]
###### party_votes ={}
###### winning_party =""
###### vote_winning_party = 0
###### percentage_winning_party = 0
###### party_name = row[4] # assumiong the information is in column 5
###### if party_name not in party_list:
###### party_list.append(party_name)
###### party_votes[party_name] = 0
###### party_votes[party_name] += 1
###### for party_name in party_votes:
###### ptyvotes = party_votes.get(party_name)
###### ptypercentage = float(ptyvotes)/float(total_votes)*100
###### party_results =(f"{party_name}: {ptypercentage:.1f}% ({ptyvotes}))
>>>>>>> 6f398ece1e3271563dd86f05496c0978814d9271

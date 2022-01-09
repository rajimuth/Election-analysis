# path = ("C:\Users\aahaa\OneDrive\Desktop\Election-analysis\Resources\election_results.csv")
# f = open(path,"r")
# print(f.read())
# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
# import csv
# dir(csv)
# import csv
# import os
# csvpath = os.path.join('Election-analysis','Resources','election_results.csv')
# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
# #     csvreader = csv.reader(csvfile, delimiter=',')

# #     print(csvreader)
# import csv
# with open('netflix_ratings.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     # with open ('newnetflix_rating.csv','w') as new_csv_file:
#     #     csv_writer = csv.writer(new_csv_file)
#     #     for line in csv_reader:
#     #       csv_writer.writerow(line)
#     for line in csv_reader:
#         print (line)
# import csv
# my_dict =[{'name':'raji' ,'sex':'female', 'quality':'energetic'},
#     {'name':'Oviya' ,'sex':'female', 'quality':'cheerful'},
#     {'name':'charan' ,'sex':'male', 'quality':'playful'},
#     {'name':'suresh' ,'sex':'male', 'quality':'mindful'}]
# fields =['name','sex','quality']
# file_name ='newnetflix_rating.csv'
# with open ('newnetflix_rating.csv','w') as new_csv_file:
#       writer = csv.DictWriter(new_csv_file, fieldnames = fields, delimiter ='\t')
#       writer.writeheader()
#       writer.writerows(my_dict)
import pandas
result = pandas.read.csv (netflix_ratings.csv)
print (result)

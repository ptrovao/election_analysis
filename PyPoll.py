# The data we need to retrieve
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os
file_to_load = os.path.join ("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

# import csv
# import os
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")


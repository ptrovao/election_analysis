# The data we need to retrieve
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our depedencies
import csv
import os
file_to_load = os.path.join ("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and Candidate vote
candidate_options = []

#1. Declare an empty dictionare
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print candidate name in each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:

            # Add candidate name to candidate's list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's name count 
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate through the counts
    #1. Iterate through candidate list
    for candidate_name in candidate_votes:

        #2. Retrieve vote count for a candidate
        votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print (candidate_results)

        # Save candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate 
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

# import csv
# import os
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")


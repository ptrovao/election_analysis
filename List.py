# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# score = int(input("What is your test score?"))
# if score >= 90:
#     print("Your grade is A")
# elif score >= 80:
#     print("Your grade is B")
# elif score >= 70:
#     print("Your grade is C")
# else:
#     print("Your grade is F")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# for county in counties.key():
#     print(counties [i])

# x = 0
# while x <= 5:
#     print (x)
#     x = x + 1

counties_dict = {}
counties_dict ["Arapahoe"] = 422829
counties_dict ["Denver"] = 463353
counties_dict ["Jefferson"] = 432438
for coun, vot in counties_dict.items():
    print (f"The disctirct of {coun} has {vot:,} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election?"))
# total_votes = int(input("What is the total number of votes in the election?"))
# message_candidate = (f"You have received {candidate_votes:,} number of votes."
#                     f"The total number of votes in the election was {total_votes:,}."
#                     f"You received {candidate_votes/total_votes*100:.2f}% of the total votes.")
# print(message_candidate)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv



# Assign a variable for the file to load and the path.
file_to_load = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Resources/election_results.csv'

# Assign a variable for the file to load and the path.
file_to_save = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Analysis/Election_Analysis.txt'

# 1. initiatlize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.    
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
       # Add to the total vote count.
       total_votes += 1

    # Print the candidate name from each row
    candidate_name = row[2]

    # If the candidate does not match any existing candidate
    #if candidate_name not in candidate_options:
        # Add the candidate name to candidate list.
        #candidate_options.append(candidate_name)

        # Begin tracking that candidate's votes.
        #candidate_votes[candidate_name] = 0

# Print the cadidate list.
#print(candidate_options)








# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Analysis/Election_Analysis.txt'












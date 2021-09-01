# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Resources/election_results.csv'

# Assign a variable for the file to load and the path.
file_to_save = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Analysis/Election_Analysis.txt'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze data here
    file_reader = csv.reader(election_data)

    # Print the header row.    
    headers = next(file_reader)
    print(headers)


# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Analysis/Election_Analysis.txt'
# Using the with statement open the file as a text file.
##outfile = open(file_to_save, "w")

#outfile write some data to file
#outfile.write("Hello World")

#close file
#outfile.close()


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = '/Users/rachelkrasner/Desktop/UCB_Data_Analysis/Module3/Election_Analysis/Analysis/Election_Analysis.txt'

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    #write some data to the file
    #txt_file.write("Counties in the election:\n ")
    #txt_file.write("-------------------------\n ")
    # Write three counties to the file.
    #txt_file.write("Arapahoe\n Denver\n Jefferson")











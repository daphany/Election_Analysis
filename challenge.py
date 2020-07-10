import csv
import os
#Assign variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
#Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)
    
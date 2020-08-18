# DNA - Program to read DNA STRs
from sys import argv, exit
import csv
import re
import itertools



# Verify if the user gave the right command-line
if len(argv) != 3:
    print("Usage: python dna.py [DATABASE FILE] [TEXT FILE DNA SEQUENCE]")
    exit(1)
# If correct command-line gave, go ahead and open database file and sequences file

# Open and read database file and extract the informations into a list
with open(argv[1], 'r') as database:
    reader = csv.reader(database)
    for row in reader:
        dnaDatabase = row
        dnaDatabase.pop(0)
        break
# Create a dictionary to store the sequences
sequences = {} 

# Transfers the informations from the list to the dictionary structure where the STR's are the keys
for item in dnaDatabase:
    sequences[item] = 1
 

# Open sequence file
with open(argv[2], 'r') as file:
    dnaSample = file.read()
    

# Loop to get STRs
for key in dnaDatabase:
    count = 0
    countMax = 0
    keyLength = len(key)
    for i in range(len(dnaSample)):
        # If it already counted one sequence, skips at the end to avoid counting again
        while count > 0:
            count -= 1
            continue
        
        # Check if the sequence of substring corresponds to the key(STR) if there's a repetition of the same STR
        if dnaSample[i: i + keyLength] == key:
            # Check for the repetition
            while dnaSample[i - keyLength: i] == dnaSample[i: i + keyLength]:
                count += 1
                i += keyLength
                
            # Check if the value of the previous longest sequence is longer than the currently, if yes, it'll override it    
            if count > countMax:
                countMax = count
    
    # Store the longest sequence found in the dictionary structure where the key is the STR
    sequences[key] += countMax
    
# Open the DNA Database again; iterate trough it like in a dictionary and compare the sequences
with open(argv[1], 'r') as database:
    dnaDatabase = csv.DictReader(database)
    for person in dnaDatabase:
        match = 0
        # Loop to compare the sequences to every person and prints his/her name if there's a match
        for dnaSample in sequences:
            if sequences[dnaSample] == int(person[dnaSample]):
                match += 1
            if match == len(sequences):
                print(person['name'])
                exit(0)
        
    
    print('No Match')
   
            
            
            
                    
            
                










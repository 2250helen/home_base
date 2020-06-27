# Set-up python environment
import os
import csv

# Identify location of data
# location = 'C:\Users\2250h\Documents\STUDY\UWA-Bootcamp\Homework\03-Python\python-challenge\PyPoll\'
source = os.path.join('resources', 'election_data.csv')
output = os.path.join('analysis', 'election_results.txt')

# reads voter data in file
def voters(n):
     # set row counter to zero
    counter = 0
    # open file to read
    with open(source) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # increment row counter
        for row in csvreader:
            counter = counter + 1
            # print current row
            print(row)
            # stop printing rown when row counter reaches max
            if counter >= n:
                break

# returns total number of votes for each elector, skipping the header 
def count_votes():
    # initialize vote counter
    totalcount = 0
    # set voter counter to zero
    counter = 0
    # open file to read
    with open(source) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # iterate over rows in .csv
        for row in csvreader:
            # pass row if it is a header
            if row[0] == 'Voter ID':
                pass
            # if not a header row, increment single file row counter
            else:
                counter = counter + 1
    # when finished counting rows in file, add to total vote counter 
    totalcount = totalcount + counter
    return totalcount

# returns a list of unique candidates
def candidate_names():
    # create list to hold unique candidates
    candidates = []
    # open file to read   
    with open(source) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # iterate over rows in .csv
        for row in csvreader:
            # skip header row
            if row[0] == 'Voter ID':
               pass
            else:
                # check to see if current candidate is in list
                if row[2] not in candidates:
                   # if new candidate, add to candidate list
                   candidates.append(row[2])
                else:
                   pass
    return candidates 

# sums the votes for each candidate and returns a dictionary: {"Candidate":[percentage, votes]}
def candidate_votes():
    # initialize dictionary
    candidatedict = {}
    # iterate over the list of unique candidates
    for candidate in candidates:
        # initialize list of 2 integers for each candidate key
        candidatedict[candidate] = [0,0]

# iterate over the election data file
    # open file to read  
    with open(source) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # iterate over rows
        for row in csvreader:
            # skip headers
            if row[0] == 'Voter ID':
                pass
            else:
                # iterate over the candidate dictionary
                for key, value in candidatedict.items():
                    # when candidate dictionary key matches voter candidate
                    if key == row[2]:
                        # increment vote value (2nd element in dict value list)
                        value[1] = value[1] + 1
                        # update percent votes for candidate in dict
                        value[0] = round(((value[1] / totalcount) * 100), 1)
                    else:
                        pass
    return candidatedict

# return the candidates name with the highest vote count value               

def findwinner():
    # initialize comparison value
    numberone = 0
    # iterate over each unique candidate in dict
    for key, value in candidatedict.items():
        # if largest vote count so far, store as top vote count
        if value[1] > numberone:
            numberone = value[1]
            # store corresponding candidate name
            winner = key
        else:
            pass
    return winner

# run above functions in sequence
totalcount = count_votes()
candidates = candidate_names()
candidatedict = candidate_votes()
winner = findwinner()

# function for easy line seperator in .txt output
def insert_newline():
    print('\n',('-' * 30))

# print results to .txt file 
def print_results():
    print('Election Results')
    insert_newline()
    print('\n', 'Total Votes:', totalcount)
    insert_newline()
# print contents of candidate dictionary with % formatting
    for key, value in candidatedict.items():
        print('\n' + key + ':', str(value[0]) + '%  (' + str(value[1]) + ')')
    insert_newline()
    print('\n' + 'Winner: ', winner)
    insert_newline()

# open output file and writes results of analysis
def write_tofile():
    with open(output, 'w', newline='') as f:
        f.write('Election Results' )
        f.write('\n' + ('-' * 30))
        f.write('\n' + 'Total Votes: ' + str(totalcount))
        f.write('\n' + ('-' * 30))
        for key, value in candidatedict.items():
            f.write('\n' + key + ': ' + str(value[0]) + '%  (' + str(value[1]) + ')')
        f.write('\n' + ('-'  * 30))
        f.write('\n' + 'Winner: ' + winner)
        f.write('\n' + ('-'* 30))

# execute the above functions to record election result
print_results()
write_tofile()
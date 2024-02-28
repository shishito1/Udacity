"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#print(texts)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers_unique = set()

# Get both to and from text numbers
for text in texts:
    numbers_unique.add(text[0])
    numbers_unique.add(text[1])

# Get both incoming and outgoing numbers
for call in calls:
    numbers_unique.add(call[0])
    numbers_unique.add(call[1])

print(f"There are {len(numbers_unique)} different telephone numbers in the records.")

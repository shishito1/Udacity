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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
non_telemarketer = set()
outgoing = set()
telemarketers = set()

# Get a set of all incoming phone calls.
for call in calls:
    outgoing.add(call[0])
    non_telemarketer.add(call[1])

for text in texts:
    non_telemarketer.add(text[0])
    non_telemarketer.add(text[0])

# Get the set of telemarketers.
telemarketers = outgoing.difference(non_telemarketer)

print('These numbers could be telemarketers: ')
print(*sorted(telemarketers), sep='\n')

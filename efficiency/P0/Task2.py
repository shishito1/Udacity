"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Create a dictionary with phone number as key.
duration_sums = dict()
for call in calls:
    # Filter for calls made in November 2016.
    if call[2].startswith('11-'):
        call_duration = int(call[-1])
        # Count the duration of outgoing and incoming calls.
        duration_sums[call[0]] = duration_sums.get(call[0], 0) + call_duration
        duration_sums[call[1]] = duration_sums.get(call[1], 0) + call_duration

# Get the largest call duration by phone number.
longest_duration_key = max(duration_sums, key=lambda key: duration_sums[key])
print(f"{longest_duration_key} spent the longest time, {duration_sums[longest_duration_key]} seconds, on the phone during September 2016.")

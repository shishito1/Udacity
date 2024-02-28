"""Write a script for a class
It takes three sets of input, converts them each to lists, 
then iterates over each list to create the message.
"""

names =  input("Enter names separated by commas: ").split(",")
assignments = input("Enter assignments separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, 
## and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades): 
    print(message
          .format(
              name.title(), 
              assignment, 
              grade, 
              int(grade) + int(assignment)*2
        ))
    
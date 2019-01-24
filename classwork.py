def main():
    # problem1()
    problem2()


# Create a function that has a loop that quits with q
#     Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names
# ADDITIONAL REQUIREMENTS:
# Your code should be able to process the quit command (q) the User enters regardless of case
def problem1():
    userinput = ""
    names = []
    while (userinput.lower() != 'q'):
        userinput= input("Enter names, Enter q to quit ")
        print(userinput)
        names.append(userinput)
        if userinput.lower() == 'q':
            break
        print(names)


# Given the following List of Dictionaries:
#
# myDictionaryList = [
#     {
#         "name": "Kelvin",
#         "age": 30
#     },
#     {
#         "name": "Bob",
#         "age": 50
#     },
#     {
#         "name": "Alex",
#         "age": 21
#     }
# ]
# Create a function that does the following when called:
#
# Prints a formatted list of names and ages
# ex.
#
# Name: Kelvin
# Age: 30
#
# Name: Bob
# Age: 50
#
# Name: Alex
# Age: 21
# Prompts the User for which property they want to use to sort the list (e.g. AGE or NAME). Print the formatted list of names and ages sorted by the specified sort criteria.
#
# Continue prompting the User for the sort criteria and print a sorted list until the User enters q then exit.
#
# ADDITIONAL REQUIREMENTS:
#
# Your code should be able to process the sort criteria the User enters regardless of case
# Your code should be able to process the quit command (q) the User enters regardless of case
# If the User enters something other than q or a valid sort criteria (e.g. AGE or NAME) your code should display INVALID ENTRY. PLEASE TRY AGAIN and continue the process.
def problem2():
    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]

    for eachEl in myDictionaryList:
        print(eachEl['name'],eachEl['age'])
    howToSort = input("How do you want to sort values?")
    if howToSort == age:
        


if __name__ == '__main__':
    main()
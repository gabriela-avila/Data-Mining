#2. a. Create a for loop that prompts the user to enter 3 different items, then appends them to new items list.
mycolors=[]                                   # It creates a new list
for i in range(3):                            # It asks three times his favorite color
    item=input("Enter your favorite color:")  # It saves the user input in item variable
    mycolors.append(item)                     # It adds item variable to mycolors list
print("These are your favorite colors:")      # It prints a header for the results
for color in mycolors:                        # It prints each color of mycolors list
    print(color)

    
#2. b. Write a program for removing duplicates from the list, append unique values to new list.
biglist=[1,2,1,3,2,4,4,5]
print("biglist =", biglist)          # It prints the big list
purgedlist=[]                        # It creates a purged list to save unique items
for i in biglist:                    # for each item in biglist, do it
    if i not in purgedlist:          # It verifies if this item is not already in the purged list
        purgedlist.append(i)         # It adds the item in the purged list
print("purgedlist =", purgedlist)    # It prints the purged list


#2. c. Write a Python function to print a list where the values are square of numbers between a and b.
def squares_between(a,b):            # It defines a function with two arguments a and b
    if a>b:                          # It verifies if a is greater than b,
        c=a                          # Then it swaps a and b
        a=b
        b=c
    squares=[]                       # It instantiates a list called squares
    for value in range(a,b+1):       # For values between a and b, do it
        square = value**2            # It calculates the square from value
        squares.append(square)       # It appends this square value at the end of the list
    return (squares)                 # It returns the list of square values

a=10                                 # It creates a and b for testing the function
b=30
sequence = squares_between(a,b)      # It assigns the sequence variable as the list of square values between a and b 
print(sequence)                      # It prints the sequence list


#2. d. Write function where two strings are given, then remove letters from first string if they are in string2.
def reduce(string1,string2):              # It defines a function with two string arguments
    result=""                             # It creates an empty string for save the result
    for i in range(len(string1)):         # For each letter of the first string, do it
        if string1[i] not in string2:     # It checks if this letter is not in the second string
            result += string1[i]          # It adds this letter to the end of the string result
    return result                         # It returns the unique letters from the first string

string1='heyhowareyou'                    # It creates an instance for the first string
string2='hurray'                          # It creates an instance for the second string
print(reduce(string1,string2))            # It prints the letters from the first string which are not in the second one

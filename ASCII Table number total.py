#This is code is meant to get input from the user and give
#the total ascii value of all letters from the user's input. 

#First to get the users input
user_word = input("Please enter word: ")

#Defining the asciiValue function
def asciiValue(user_word):

    #A counter to keep track of the total
    counter = 0

    #Converting the users input to a string to iterate through
    string_list = list(user_word)

    #Iterating through the string
    for i in string_list:

        #Getting the ordinal value of each iterated value
        num_val = ord(i)

        #Adding ordinal value to the counter
        counter += num_val
    print(counter)

asciiValue(user_word)

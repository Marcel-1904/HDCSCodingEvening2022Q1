#This is a very simple calculator application only capable of 2 value equations without any UI

#Gettting the first number of input from the user
first_num = int(input("Please enter first number: "))

#The symbol for the math equation
symbol = input("Please enter the symbol for your equasion: ")

#Second number of input from user
second_num = int(input("Please enter the second  number: "))

#For addition
if symbol == "+":
    answer = first_num + second_num
    print(answer)
    print("")

#For subtraction
elif symbol == "-":
    answer = first_num - second_num
    print(answer)

#For multiplication
elif symbol == "x":
    answer = first_num * second_num
    print(answer)

#For division
elif symbol == "/":
    answer = first_num / second_num
    print(answer)
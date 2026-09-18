#Create a variable named x and store an integer (whole number) inside it
x = 10
# Create a variable named y and store a string (any characters between single or double quotes) inside it
y = "Hello"
# Create a variable named z and store a float in it
z = 2.2
# Change the value stored in the x variable to a new string
x = "Coffee"
# Change the value stored in the y variable to a new boolean
y = True
# Change the value store in the z variable to a different float
z = 5.3
# Print the value the user entered from the previous section
Answer = input("What is your answer:")
print(Answer)
# Print the (current) value of the variable x
print(x)
# Print the *type* (not the value itself) of the value stored in the y variable
print(type(y))
# Create two variables, one containing the string CIT, and another containing the string 1515
course = "CIT"
number = "1515"
# Using the two variables and a hard-coded letter, print the word ACIT1515 to the terminal
print("A" + course + number)
#Alternately, you can use an "f" string (properly referred to as a string literal) to print out the values of variables within a string
#To create an f-string, put the letter f before your quotes - any values you want to print out insdie the quotes must be surronded with braces {}. try gettring the below to work:
assignment_number = 2
print(f'Assignment {assignment_number} created')
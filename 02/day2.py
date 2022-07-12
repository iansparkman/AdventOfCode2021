## advent of code 2021 day 02
## still in my submarine

# open our data file
data = open("02/input.txt", "r", encoding="utf-8")

# read the data file and split the contents by new lines
data = data.read().splitlines()

# make data a list, and for each item in the data, split that into two components which themselves are a list
# this is technically an array, a list of lists where each list item is a list of strings, like:
# [ ['forward', '4'] , ['forward', '8'] , ['down', '2'] , ... , ['up', '3'] ]
data = [x.split() for x in data]

# this one is a little tricky...
# make a list called commands from the data list, where each item in the list now is a tuple containing the command as a string and the value as an integer
# this ends up looking like:
# [ ('forward', 4) , ('forward', 8) , ('down', 2) , ... , ('up', 3) ]
commands = [ ( x[0] , int(x[1]) ) for x in data ]

# instantiate these two variables we will modify while going through the information
horizontal, depth = 0 , 0

# go through the list of commands, and for each tuple (command and value):
for command, value in commands:

    # if command is forward, add the value to horizontal
    if command =='forward':
        horizontal += value

    # if command is down, add the value to depth
    elif command == 'down':
        depth += value

    # if command is up, subtract the value from depth
    elif command == 'up':
        depth -= value

# lastly, multiply our results of horizontal and depth
endResult = horizontal * depth

print("PART 1: multiplying horizontal position * depth gives: " + str(endResult))


#############################################################################

## PART 2
## this one is almost exactly the same as part 1, but the addition of the 'aim' parameter
## changes how we alter the 'horizontal' and 'depth' values when looping through the list of commands

data = open("02/input.txt", "r", encoding="utf-8")

data = data.read().splitlines()

data = [x.split() for x in data]

commands = [(x[0], int(x[1])) for x in data]

aim, horizontal, depth = 0 , 0 , 0

for command, value in commands:

    # add value to horizontal, and add product of value and aim to depth
    if command =='forward':
        horizontal += value
        depth += value*aim

    # add value to aim
    elif command == 'down':
        aim += value

    # subtract value from aim
    elif command == 'up':
        aim -= value

endResult2 = horizontal * depth

print("PART 2: with aim, multiplying horizontal position * depth gives: " + str(endResult2))
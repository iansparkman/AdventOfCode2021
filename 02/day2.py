## advent of code 2021 day 02
## still in my submarine

data = open("input", "r", encoding="utf-8")

data = data.read().splitlines()

data = [x.split() for x in data]

commands = [(x[0], int(x[1])) for x in data]

horizontal, depth = 0 , 0

for command, value in commands:
    if command =='forward':
        horizontal += value
    elif command == 'down':
        depth += value
    elif command == 'up':
        depth -= value

endResult = horizontal * depth

print("PART 1: multiplying horizontal position * depth gives: " + str(endResult))


#############################################################################

## PART 2

data = open("input", "r", encoding="utf-8")

data = data.read().splitlines()

data = [x.split() for x in data]

commands = [(x[0], int(x[1])) for x in data]

aim, horizontal, depth = 0 , 0 , 0

for command, value in commands:

    if command =='forward':
        horizontal += value
        depth += value*aim

    elif command == 'down':
        aim += value

    elif command == 'up':
        aim -= value

endResult2 = horizontal * depth

print("PART 2: with aim, multiplying horizontal position * depth gives: " + str(endResult2))
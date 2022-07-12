## Advent of Code 2021 day 1
## Look through the data, and count how many times the numbers increase from one to the next (as opposed to decrease)
## In the test list below, there are 8 times this happens

# test list
# data = [119, 121, 129, 128, 130, 134, 138, 143, 113, 114, 129]

# real list
# https://adventofcode.com/2021/day/1

# open file containing data to look at (make sure file is in same directory as this program)
file = open("data.txt", "r", encoding="utf-8")

# stick that info in a variable called data
data = file.read().splitlines()

# iterate through items in data, putting each into a list called depths (making sure items' data type is integer)
depths = [int(x) for x in data]

# the number of increases is the sum of the number of times that one item is less than the next--
increases = sum(x < y for x, y in zip(depths, depths[1:]))

print("the number of single-measurement depth increases is : " + str(increases))

########################################################################################################

# part two! check the number of times this increasing thing happens, but between sliding sindows of three measurements
# conveniently, the equivalent of: depths[n] + depths[n+1] + depths[n+2] < depths[n+1] + depths[n+2] + depths[n+3]
# is just: depths[n] < depths[n+3]
# so we just need to compare each measurement to the one two away rather than the one right next to it

increases_window = sum(x < y for x, y in zip(depths, depths[3:]))

print("the number of sliding-window-measurement depth increases is : " + str(increases_window))
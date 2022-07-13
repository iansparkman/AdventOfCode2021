## advent of code 2021 day 3
## finding the most and least common bit in a certain position over a long list of binary numbers
## then the most common and least common bits across the board go together to make the gamma and epsilon rates in binary
## multiply those two numbers together in decimal form to get power consumption

# open the data file, split by new lines
data = open('03/input.txt', 'r', encoding='utf-8').read().splitlines()

# get length of each line
N = len(data[0])

# set up our gamma and epsilon numbers as empty lists of zeros as long as each data entry
gamma = [0] * N
epsilon = [0] * N

# for each element position in a line of the data...
for i in range(N):

    # set counters for zeros and ones
    zero = 0
    one = 0

    # for each line in the data
    for j in range(len(data)):

        # if the element at this position is 0 or 1, add to the respective counter for that line
        if data[j][i] == '0':
            zero += 1
        if data[j][i] == '1':
            one += 1

    # if there are more zeros than ones in this position for the whole list, set gamma to zero and epsilon to one at that position:
    if zero > one:
        gamma [i] = '0'
        epsilon[i] = '1'
    # if there are more ones than zeros in this position for the whole list, set gamma to one and epsilon to zero at that position:
    elif one > zero:
        gamma[i] = '1'
        epsilon[i] = '0'

# get gamma and epsilon numbers as decimal--join elements of the gamma and epsilon lists, convert to integer from base 2 (binary)
decimal_gamma = int(''.join(gamma), 2)
decimal_epsilon = int(''.join(epsilon), 2)

power = decimal_epsilon * decimal_gamma

print("The power consumption is: " + str(power))
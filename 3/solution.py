def getMostAndLeastCommonBits(lines):
    vals = [0] * (len(lines[0]) - 1)
    gamma = ""
    epsilion = ""
    print("Line len: ", len(lines[0]))
    for line in lines: 
        for i in range(len(line) - 1):
            if line[i] == '0':
                vals[i] -= 1
            else:
                vals[i] += 1

    for i in range(len(vals)):
        if vals[i] > 0:
            gamma += str(1)
            epsilion += str(0)
        else:
            gamma += str(0)
            epsilion += str(1)
    print(vals)
    return [gamma, epsilion]

def calculateMostAndLeastCommonBit(lines, bit_number):
    count = 0
    bits = [0, 0]
    for line in lines:
        if line[bit_number] == '0':
            count -= 1
        else:
            count += 1

    if count < 0:
        bits = ["0", "1"]
    else:
        bits = ["1", "0"]
    return bits

def oxygenGeneratorRating(lines):
    for it in range(len(lines[0]) - 1):
        bits = calculateMostAndLeastCommonBit(lines, it)
        lines = [i for i in lines if i[it] == bits[0]]
        if len(lines) == 1:
            return lines
    return lines

def co2ScrubberRating(lines):
    for it in range(len(lines[0]) - 1):
        bits = calculateMostAndLeastCommonBit(lines, it)
        lines = [i for i in lines if i[it] == bits[1]]
        if len(lines) == 1:
            return lines
    return lines

file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

result = getMostAndLeastCommonBits(lines)
gamma = int(result[0], 2)
epsilion = int(result[1], 2)


result = gamma * epsilion
print("Result: ", result)

oxygen_rating = oxygenGeneratorRating(lines)
oxygen_rating = oxygen_rating[-1]
co2_rating = co2ScrubberRating(lines)
co2_rating = co2_rating[-1]
res_part_two = int(oxygen_rating, 2) * int(co2_rating, 2)
print(oxygen_rating, "co2", co2_rating)
print("Result part two: ", res_part_two)



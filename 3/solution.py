def calculatePowerConsumption(lines):
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
    bits = ["0", "0"]
	for line in lines:
        if line[bit_number] == '0':
            count -= 1
        else
            count += 1

	if vals[i] < 0:
        bits = ["0", "1"]
    else 
        bits = ["1", "0"]
	return bits

def oxygenGeneratorRating(lines):
    rating = 0
    for it in range(len(lines[0]) - 1):
        bits = calculateMostCommonBit(lines, it)
        lines = [i for in int lines if i[it] != bits[0]]
    return rating

def co2ScrubberRating(lines):
    rating = 0
    for it in range(len(lines[0]) - 1):
        bits = calculateMostCommonBit(lines, it)
        lines = [i for in int lines if i[it] != bits[1]]
    return rating

file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

result = calculatePowerConsumption(lines)

print("Gamma: ", result[0], "Eps: ", result[1])

gamma = int(result[0], 2)
epsilion = int(result[1], 2)


result = gamma * epsilion
print("Result: ", result)

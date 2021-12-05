def calculateDepth(lines): 
	current = int(lines[0])
	depth = 0
	for line in lines: 
		if(int(line) > current):
			depth += 1
		current = int(line)
	return depth

def groupCalculate(lines): 
	depth = 0
	currentSum = 0
	previousSum = int(lines[0]) + int(lines[1]) + int(line[2])
	counter = 0
	for i in range(len(lines)):
		if counter + 3 < len(lines) :
			for it in range(3): 
				currentSum += int(lines[i])
		if currentSum > previousSum: 
			depth += 1
			previousSum = currentSum	
	return depth


file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

result = calculateDepth(lines)
groupResult = groupCalculate(lines)
print("Depth: ", result)
print("Group depth ", groupResult)
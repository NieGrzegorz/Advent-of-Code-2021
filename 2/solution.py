def pilot(lines): 
	horizontal = 0
	depth = 0
	for line in lines: 
		var = line.split() 
		if var[0] == 'forward':
			horizontal += int(var[1]) 
		elif var[0] == 'down':
			depth += int(var[1])
		elif var[0] == 'up': 
			depth -= int(var[1])
	return (depth * horizontal)

def secondPilot(lines): 
	aim = 0
	depth = 0
	horizontal = 0

	for line in lines: 
		var = line.split() 
		if var[0] == 'forward':
			horizontal += int(var[1])
			depth = depth + (aim * int(var[1]))
		elif var[0] == 'down':
			aim += int(var[1])
		elif var[0] == 'up': 
			aim -= int(var[1])
	return depth * horizontal

file_name = "input.txt"
file_hook = open(file_name); 
lines = file_hook.readlines()

result = pilot(lines)
secondPilotResult = secondPilot(lines)

print("Result: ", result)
print("Second pilot result: ", secondPilotResult)

day = 1

def parseLines(lines): 
    lines = lines[-1]
    lines = lines[:-1]
    lines = lines.split(',')
    int_map = map(int, lines)
    lines = list(int_map)
    return lines

def calculateInternalTimer(fish): 
    new_list = []
    for timer in fish: 
        timer -= 1
        new_list += [timer]
    return new_list 

def spawnFish(fish_list): 
    count = 0 
    new_list = []
    for fish in fish_list:
        if fish == -1:
            count += 1
            fish = 6
        new_list += [fish]
    new_list += ([8] * count)
    return new_list


file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

lines = parseLines(lines)

while day <= 256:
    lines = calculateInternalTimer(lines)
    lines = spawnFish(lines)
    day += 1
    print("Day: ", day)

print(len(lines))

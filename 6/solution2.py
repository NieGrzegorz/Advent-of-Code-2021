day = 1
max_day = 80

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
    return [count, new_list]

def countDescendants(count, days_left):
    result = count
    if days_left >= 8:
        result += countDescendants(count, days_left - 8)
        days_left -= 8 
        while days_left >= 6: 
            result += countDescendants(count, days_left - 6)
            days_left -= 6
        return result
    else:
        return result

file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

lines = parseLines(lines)
final_fish = len(lines)
while day <= max_day:
    lines = calculateInternalTimer(lines)
    result = spawnFish(lines)
    count = result[0]
    lines = result[1]
    final_fish += countDescendants(count, (max_day - day))
    day += 1


print(final_fish)

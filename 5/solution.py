globalMap = [[0] * 1000 for _ in range(1000)]

def addPointsToMap(pointA, pointB):
    if pointA[0] == pointB[0] and pointA[1] == pointB[1]: 
        globalMap[pointA[0]][pointA[1]] += 1
    elif pointA[0] == pointB[0]:
        larger = max(pointA[1], pointB[1])
        smaller = min(pointA[1], pointB[1])
        for i in range(smaller, larger + 1):
            globalMap[pointA[0]][i] += 1
    elif pointA[1] == pointB[1]:
        larger = max(pointA[0], pointB[0])
        smaller = min(pointA[0], pointB[0])
        for i in range(smaller, larger + 1):
            globalMap[i][pointA[1]] += 1
    else: 
        tempA = pointA
        while tempA[0] != pointB[0] and tempA[1] != pointB[1]:
            globalMap[tempA[0]][tempA[1]] += 1
            
            if tempA[0] > pointB[0]:
                tempA[0] -= 1
            else:
                tempA[0] += 1

            if tempA[1] > pointB[1]:
                tempA[1] -= 1
            else:
                tempA[1] += 1

        globalMap[pointB[0]][pointB[1]] += 1

def drawLines(lines):
    for pair in lines:
        addPointsToMap(pair[0], pair[1])

def parseIntoPairs(lines):
    new_lines = []
    for line in lines:
        new_lines += line.split()

    new_lines = [i for i in new_lines if i != "->"]
    lines = []
    for pair in range(0,len(new_lines),2):
        lines += [[new_lines[pair], new_lines[pair + 1]]]
    new_lines = []
    points = []
    for pair in lines:
        points += [pair[0].split(',')]
        points  += [pair[1].split(',')]
        new_lines += [[[int(points[0][0]), int(points[0][1])], [int(points[1][0]), int(points[1][1])]]]
        points = []
    return new_lines

def countIntersections():
    count = 0
    for i in range(0,1000):
        for j in range(0,1000):
            if globalMap[i][j] >= 2:
                count += 1
    return count

file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines()

lines = parseIntoPairs(lines)
print(lines[0], lines[-1])

drawLines(lines)
# addPointsToMap([1, 2], [1,5])
count = countIntersections()
print(count)
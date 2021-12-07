def parseBoard(board):
    parsed_board = []
    for line in board: 
        line = line[:-1]
        line = line.split()
        to_insert = []
        for character in line: 
            to_insert += [[character, False]]
        parsed_board += [to_insert]
    return parsed_board

def parseBoards(boards):
    parsed_boards = []
    for board in boards: 
        parsed_boards += [parseBoard(board)]
    return parsed_boards

def applyNumber(board, number): 
    new_board = []
    for line in board:
        new_line = []
        for character in line: 
            if character[0] == number: 
                new_line += [[character[0], True]]
            else:
                new_line += [character]
        new_board += [new_line]
    return new_board

def checkWinningCondition(board):
    for line in board:
        count = 0
        for element in line: 
            if element[1] == True:
                count += 1
        if count == len(board[0]):
            return True

    for i in range(len(board[0])):
        count = 0
        for j in range(len(board)):
            if board[j][i][1] == True:
                count += 1
        if count == len(board[0]):
            return True
    return False

def playNumber(board_list, number):
    new_board_list = []
    for board in board_list:
        new_board_list += [applyNumber(board, number)]
    return new_board_list

def checkResults(boards):
    winningBoards = []
    for board in boards: 
        result = checkWinningCondition(board)
        if result == True:
            return [True, board]
    return[False, 0, 0]

def sumUnmarked(board):
    result = int(0)
    for line in board:
        for element in line:
            if element[1] == False:
                result += int(element[0])
    return result

def getWinningBoards(boards):
    winningBoards = []
    for board in boards:
        result = checkWinningCondition(board)
        if result == True:
            winningBoards += [board]
    return winningBoards

def playGamePartOne(bingo_numbers, board_list): 
    for number in bingo_numbers:
        board_list = playNumber(board_list, number)
        result = checkResults(board_list)
        if(result[0] == True):
            score = sumUnmarked(result[1])
            score = score * int(number)
            print(score, number)
            break

def letWin(bingo_numbers, board_list): 
    for number in bingo_numbers: 
        board_list = playNumber(board_list, number)
        winningBoards = getWinningBoards(board_list)
        for board in winningBoards:
            score = sumUnmarked(board)
            score = score * int(number)
            print(score)
            board_list.remove(board)


file_name = "input.txt"
file_hook = open(file_name, 'r')
lines = file_hook.readlines() 

bingo_numbers = lines[0]
bingo_numbers = bingo_numbers[:-1]
bingo_numbers = bingo_numbers.split(',')

boards = lines[1:]
boards = [i for i in boards if i[0] != "\n"]
board_list = []

for it in range(0,len(boards),5):
    board_list += [boards[it:it+5]]

board_list = parseBoards(board_list)
letWin(bingo_numbers, board_list)





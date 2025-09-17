import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print("   ", end=" |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def getAvailableRow(col):
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][col] == "":
            return row
    return None

def checkWin(player):
    # Horizontal check
    for row in range(rows):
        for col in range(cols - 3):
            if all(gameBoard[row][col + i] == player for i in range(4)):
                return True
    # Vertical check
    for row in range(rows - 3):
        for col in range(cols):
            if all(gameBoard[row + i][col] == player for i in range(4)):
                return True
    # Diagonal / check
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(gameBoard[row - i][col + i] == player for i in range(4)):
                return True
    # Diagonal \ check
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(gameBoard[row + i][col + i] == player for i in range(4)):
                return True
    return False

def isDraw():
    return all(gameBoard[0][col] != "" for col in range(cols))

# Game loop
turnCounter = 0
while True:
    printGameBoard()
    currentPlayer = "🔴" if turnCounter % 2 == 0 else "🔵"
    print(f"\n{currentPlayer}'s Turn")
    
    move = input("Choose a column (A-G): ").upper()
    if move not in possibleLetters:
        print("❌ Invalid column. Please choose from A to G.")
        continue

    colIndex = possibleLetters.index(move)
    rowIndex = getAvailableRow(colIndex)

    if rowIndex is None:
        print("⚠️  Column is full. Try a different one.")
        continue

    modifyTurn((rowIndex, colIndex), currentPlayer)

    if checkWin(currentPlayer):
        printGameBoard()
        print(f"\n🎉 Player {currentPlayer} wins! Congratulations!")
        break

    if isDraw():
        printGameBoard()
        print("\n🤝 It's a draw!")
        break

    turnCounter += 1

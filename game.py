from random import randint

board = [[], [], [], [], [], [], [], []]

class Square:
    player = None
    graphic = "[ ]"
    hasMine = False

    def __init__(self, hasMine):
        self.hasMine = (True == hasMine)
        if self.hasMine:
            self.graphic = "[*]"

    def addPlayer(self, player):
        self.player = player
        self.graphic = "[P]"

    def removePlayer(self):
        self.player = None
        if self.hasMine:
            self.graphic = "[X]"
        else:
            self.graphic = "[-]"

def printboard():
    for rowIndex in xrange(7, -1, -1):
        rowView = ""
        for col in board:
            rowView += col[rowIndex].graphic
        print rowView

# set up new board
for column in board:
    colMineCount = 0
    while len(column) < 8:
        hasMine = randint(0, 1) == 1
        if len(column) != 0:
            if colMineCount == 2:
                column.append(Square(False))
            else:
                column.append(Square(hasMine))
        else:
            if board.index(column) == 0:
                column.append(Square(False))
            else:
                if hasMine:
                    column.append(Square(True))
                else:
                    column.append(Square(False))

        if column[-1].hasMine:
            colMineCount += 1


# set up player
class Player():
    x = 0
    y = 0
    uid = 2
    lives = 2


player = Player()

# place player on board
board[player.x][player.y].addPlayer(player)


def removePlayerFromBoard():
    # remove player from board
    board[player.x][player.y].removePlayer()


def getMove():
    # allow input to move player
    move = raw_input("Move: up, down, left, right?")
    movePlayer(move)


def movePlayer(move):
    removePlayerFromBoard()
    if move == "u":
        player.y += 1
    elif move == "d":
        if player.y != 0:
            player.y -= 1
    elif move == "l":
        if player.x != 0:
            player.x -= 1
    elif move == "r":
        if player.x != 7:
            player.x += 1
    else:
        print "Invald direction, try again."
        getMove()

    # is there a mine?
    if board[player.x][player.y].hasMine:
        player.lives -= 1
        if player.lives == 0:
            print "Hit a land mine and you can take no more, you're dead!"
            quit()
        else:
            print "Stood on a land mine but you limp on!"
            print "You can only take one more hit so be careful!"

    # place player on board
    board[player.x][player.y].addPlayer(player)

    if player.y == 7:
        printboard()
        print "You won!!"
        quit()
    else:
        printboard()
        getMove()


printboard()
getMove()
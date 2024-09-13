'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose:
'''
from Ship import Ships

class Map:
    def __init__(self):
        self.map = [[" " for i in range(10)] for j in range(10)]
        self.ships = []
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


    def placeShip(self, length, row, col, direction):
        direction = direction.lower()
        if direction not in ['left', 'right', 'up', 'down']:
            return False

        if row < 0 or row >= len(self.map) or col < 0 or col >= len(self.map[0]):
            return False
        if direction == 'right':
            end = col + length
            if end > len(self.map[0]):
                return False
            section = [self.map[row][ncol] for ncol in range(col, end)]

        elif direction == 'left':
            end = col - length
            if end < -1:
                return False
            section = [self.map[row][ncol] for ncol in range(end + 1, col + 1)]

        elif direction == 'down':
            end = row + length
            if end > len(self.map):
                return False
            section = [self.map[nrow][col] for nrow in range(row, end)]

        elif direction == 'up':
            end = row - length
            if end < -1:
                return False
            section = [self.map[nrow][col] for nrow in range(end + 1, row + 1)]

        possible = all(element == " " for element in section)
        if possible:
            ship = Ships(length)
            if direction == 'right':
                for new_col in range(col, end):
                    ship.updatelocation(row, new_col)
                    self.map[row][new_col] = length


            elif direction == 'left':
                for new_col in range(end + 1, col + 1):
                    ship.updatelocation(row, new_col)
                    self.map[row][new_col] = length

            elif direction == 'down':
                for new_row in range(row, end):
                    ship.updatelocation(new_row, col)
                    self.map[new_row][col] = length

            elif direction == 'up':
                for new_row in range(end + 1, row + 1):
                    ship.updatelocation(new_row, col)
                    self.map[new_row][col] = length
            self.ships.append(ship)

            return True

        return False
    def updatePlayerMap(self,row,col, opponent):
        if self.map[row][col] == "X":
            return False
        if self.map[row][col] == 1 or self.map[row][col] == 2 or self.map[row][col] == 3 or self.map[row][col] == 4 or self.map[row][col] == 5:
            self.map[row][col] = 'X'
            for ship in self.ships:
                if [row, col] in ship.locations:
                    ship.hit()
        else:
            self.map[row][col] = 'O'
        pass

    def updateOpponentMap(self, row, col, opponent):
        if self.map[row][col] =="X":
            return False
        if opponent.playerMap.map[row][col] == 1 or opponent.playerMap.map[row][col] == 2 or opponent.playerMap.map[row][col] == 3 or opponent.playerMap.map[row][col] == 4 or opponent.playerMap.map[row][col] == 5:
            self.map[row][col] = "X"
            print("><><><>< SHIP HAS BEEN HIT!!! ><><><><")
            for ship in opponent.playerMap.ships:
                if [row, col] in ship.locations:
                    if ship.sunk == True:
                        print("YOU HAVE SUNK A SHIP!")
                        for [row, col] in ship.locations:
                            self.map[r][c] = ship.length
                            return 2
                    break
            return 1
        else:
            self.map[row][col] = 'O'
            print("SHOT HAS MISSED!!! :(")
            return 0

    def display(self):
        print("  ", end="")
        for element in self.col:
            print(element, end=" ")
        print("")
        i = 0
        for list in self.map:
            print(self.rows[i], end="")
            print("|", end="")
            for element in list:
                print(element, end="|")
            print("")
            print(" ---------------------")
            i += 1
        pass
        pass

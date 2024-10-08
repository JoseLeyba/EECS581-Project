'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/15/2024
Purpose: Class for a map
'''
from Ship import Ships          #imports the ships file
from tabulate import tabulate   #imports tabulate to format the tables

#map class
class Map:              
    def __init__(self):
        self.map = [[" " for i in range(10)] for j in range(10)]        #10x10 grid with empty spaces
        self.ships = []                                                 #empty list for the ships
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                     #rows list with the given number position from 1-10
        self.col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]   #columns list with the given letter position from A-J


    def placeShip(self, length, row, col, direction):                   #function to place the ships
        direction = direction.lower()                                   #makes the direction name into lowercase when they put in left, right, up or down
        if direction not in ['left', 'right', 'up', 'down']:            #if the user doesn't put any of these directions
            return False                                                #returns it to false

        if row < 0 or row >= len(self.map) or col < 0 or col >= len(self.map[0]):   #if the row and column is less than 0 or greater
            return False
        if direction == 'right':                                                    #if the user puts in the direction of right
            end = col + length                                                      #calculates the endpoint of ship placement
            if end > len(self.map[0]):                                              #if the endpoint off the board
                return False
            section = [self.map[row][ncol] for ncol in range(col, end)]             #checks the sections are good for ship placement

        elif direction == 'left':                                                   #if user puts in the direction of left
            end = col - length                                                      #calculates the endpoint of ship placement
            if end < -1:                                                            #if endpoint is off the board
                return False
            section = [self.map[row][ncol] for ncol in range(end + 1, col + 1)]     #checks the sections are good for ship placement

        elif direction == 'down':                                                   #if user puts in the direction of down
            end = row + length                                                      #calculates the endpoint of ship placement
            if end > len(self.map):                                                 #if the endpoint off the board
                return False
            section = [self.map[nrow][col] for nrow in range(row, end)]             #checks the sections are good for ship placement

        elif direction == 'up':                                                     #if user puts in the direction of up
            end = row - length                                                      #calculates the endpoint of ship placement
            if end < -1:                                                            #if the endpoint off the board
                return False    
            section = [self.map[nrow][col] for nrow in range(end + 1, row + 1)]     #checks the sections are good for ship placement

        possible = all(element == " " for element in section)                       #checks if spaces are empty 
        if possible:                                                                #if empty, ship can be placed
            ship = Ships(length)                                                    #ship variable to create a new ship from the length
            if direction == 'right':                                                #direction is right
                for new_col in range(col, end):                                     #goes through the columns 
                    ship.updatelocation(row, new_col)                               #updates the ship's location
                    self.map[row][new_col] = length                                 #places the ship


            elif direction == 'left':                                               #direction is left
                for new_col in range(end + 1, col + 1):                             #goes through the columns 
                    ship.updatelocation(row, new_col)                               #updates the ship's location
                    self.map[row][new_col] = length                                 #places the ship

            elif direction == 'down':                                               #direction is down
                for new_row in range(row, end):                                     #goes through the row
                    ship.updatelocation(new_row, col)                               #updates the ship's location
                    self.map[new_row][col] = length                                 #places the ship

            elif direction == 'up':                                                 #direction is up
                for new_row in range(end + 1, row + 1):                             #goes through the row
                    ship.updatelocation(new_row, col)                               #updates the ship's location
                    self.map[new_row][col] = length                                 #places the ship
            self.ships.append(ship)                                                 #adds the ship to the list

            return True                                                             #returns true if successful

        return False                                                                #returns false if not successful

    def updatePlayerMap(self,row,col, opponent):                                    #function to update the player's map
        if self.map[row][col] == "X" or self.map[row][col] == 'O':                  #if the spot has been targeted
            return 0    
        if isinstance(self.map[row][col], int):                                     #if the ship is hit
            self.map[row][col] = 'X'                                                #marks the spot with an X
            for ship in self.ships:                                                 #goes through each ship in the list
                if [row, col] in ship.locations:                                    #if there's a hit part of the ship
                    ship.hit()                                                      #hit on the ship
        else:
            self.map[row][col] = 'O'                                                #marks the spot as a miss with 0
        return 1                                                                    #returns 1 if valid

    def updateOpponentMap(self, row, col, opponent):                                #function to update the opponent's map         
        if self.map[row][col] == "X" or self.map[row][col] == 'O' or self.map[row][col] == 1 or self.map[row][col] == 2 or self.map[row][col] == 3 or self.map[row][col] == 4 or self.map[row][col] == 5:
            return 0                                                                #if the spot has been target or has a ship part
        if opponent.playerMap.map[row][col] == "X":                                 #if player hits the opponent's ship
            self.map[row][col] = "X"                                                #marks with an x
            print("><><><>< SHIP HAS BEEN HIT!!! ><><><><")                         #prints the message

            for ship in opponent.playerMap.ships:                                   #goes through a loop in the opponent's ship
                if [row, col] in ship.locations:                                    #if there's a hit in the ship's park
                    if ship.sunk:                                                   #if ship is fully hit
                        print("YOU HAVE SUNK A SHIP!")                              #prints the message
                        for [srow, scol] in ship.locations:                         #goes through the ships location
                            self.map[srow][scol] = ship.length                      #marks the ship's location
                        return 2                                                    #returns 2 that the ship is sunk
            return 1                                                                #returns 1 if hit, but not sunk
        else:                                                                       #if the player misses the opponent's ship
            self.map[row][col] = 'O'                                                #marks it as a 0
            print("SHOT HAS MISSED!!! :(")                                          #prints the message
            return 1                                                                #returns 1 for miss


    def display(self):                                                              #function to display the player's map
        header = [""] + self.col                                                    #header variable for the columns
        table_data = []                                                             #empty list to store the data of table
        for i, row in enumerate(self.map):                                          #goes through the rows of the map
            table_data.append([self.rows[i]] + row)                                 #adds each row with its row number
        table = tabulate(table_data, headers=header, tablefmt="grid")               #creates the formatted table
        print(table)                                                                #prints the table

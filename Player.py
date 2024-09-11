'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
from Map import Map
class Player:
    def __init__(self):
        self.playerMap = Map()
        self.opponentMap = Map()
        self.fleetNum = 0
        
    def displayMaps(self):
        #display both boards
        print('Your Board')
        self.playerMap.display()
        print('Opponents Board')
        self.opponentMap.display()

    def addToFleet(self,length,direction,start):
        self.playerMap.placeShip(length,direction,start)
        self.fleetNum += 1
        self.playerMap.display()

    def updateOpponent(self,row,col):
        #Update the map 
        result = self.opponentMap.updateOpponentMap(row,col)
        self.opponentMap.display()
        return result
    
    def updatePlayer(self,row,col):
        #Update the map
        self.playerMap.updatePlayerMap(row,col)

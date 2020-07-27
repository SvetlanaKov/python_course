import random
import time
import os
from random import randint

class Item():
    _xCord = 1
    _yCord = 1
    _cellSymb = ""
    _step = 1
    _shot = 1
    _direction ="north"
    _dialWrongWay = ""
    def __init__(self, arena):
        self.arena = arena
    def getX(self):
        return self._xCord
    def getY(self):
        return self._yCord
    def getSymb(self):
        return self._cellSymb
    def getDir(self):
        return self._direction
    def setX(self, x):
        self._xCord = x
    def setY(self, y):
        self._yCord = y

    def isRightDirection(self, direction, item2):
        if (direction == 'w'):
            if (self._yCord - self._step > 0):
               if (self._xCord == item2.getX() and self._yCord - self._step == item2.getY()):
                   return False
               else:
                   return True
            else:
                return False
        elif(direction == 's'):
            if(self._yCord + self._step < self.arena.hight - 1):
                if (self._xCord == item2.getX() and self._yCord + self._step == item2.getY()):
                    return False
                else:
                    return True
            else:
                return False
        elif(direction == 'a'):
            if(self._xCord - self._step > 0):
                if(self._yCord == item2.getY() and self._xCord - self._step == item2.getX()):
                    return False
                else:
                    return True
            else:
                return False
        elif(direction == 'd'):
            if(self._xCord + self._step < self.arena.width - 1):
                if (self._yCord == item2.getY() and self._xCord + self._step == item2.getX()):
                    return False
                else:
                    return True
        elif(direction == 'q'):
            if ((self._yCord - self._step > 0) and (self._xCord - self._step > 0)):
                if (self._yCord - self._step == item2.getY() and self._xCord - self._step == item2.getX()):
                    return False
                else:
                    return True
        elif (direction == 'e'):
            if ((self._yCord - self._step > 0) and (self._xCord + self._step < self.arena.width - 1)):
                if (self._yCord - self._step == item2.getY() and self._xCord + self._step == item2.getX()):
                    return False
                else:
                    return True

    def move(self, direction, item2):
        if (self.isRightDirection(direction, item2)):
            self.arena.setDialog("ENTER THE COMMAND")
            if (direction == 'w'):
                self._yCord -= self._step
                self._direction = 'north'
            elif (direction == 's'):
                self._yCord += self._step
                self._direction = 'south'
            elif (direction == 'a'):
                self._xCord -= self._step
                self._direction = 'west'
            elif (direction == 'd'):
                self._xCord += self._step
                self._direction = 'east'
            elif (direction == 'q'):
                self._yCord -= self._step
                self._xCord -= self._step
                self._direction = 'north-west'
            elif (direction == 'e'):
                self._yCord -= self._step
                self._xCord += self._step
                self._direction = 'north-east'
        else:
            self.arena.setDialog(self._dialWrongWay)

    def shoot(self, bang):
        if (self._direction == 'north'):
            if (self._yCord - self._shot > 0):
                bang.setY(self._yCord - self._shot)
            else:
                self.arena.setDialog("WRONG SHOT")
        elif (self._direction == 'south'):
            if (self._yCord + self._shot < self.arena.hight - 1):
                bang.setY(self._yCord + self._shot)
            else:
                self.arena.setDialog("WRONG SHOT")
        elif (self._direction == 'west'):
            if (self._xCord - self._shot > 0):
                bang.setX(self._xCord - self._shot)
            else:
                self.arena.setDialog("WRONG SHOT")
        elif (self._direction == 'east'):
            if (self._xCord + self._shot < self.arena.width - 1):
                bang.setX(self._xCord + self._shot)
            else:
                self.arena.setDialog("WRONG SHOT")
        elif (self._direction == 'north-west'):
            if (self._yCord - self._shot > 0 and self._xCord - self._shot > 0):
                bang.setY(self._yCord - self._shot)
                bang.setX(self._xCord - self._shot)
            else:
                self.arena.setDialog("WRONG SHOT")
        elif (self._direction == 'north-east'):
            if (self._yCord - self._step > 0 and self._xCord + self._step < self.arena.width - 1):
                bang.setY(self._yCord - self._step)
                bang.setX(self._xCord + self._step)
            else:
                self.arena.setDialog("WRONG SHOT")


class Bang:
    def __init__(self, tank):
        self._tank = tank
        self._xCord = self._tank.getX()
        self._yCord = self._tank.getY()
    def getX(self):
        return self._xCord
    def getY(self):
        return self._yCord
    def setX(self, x):
        self._xCord = x
    def setY(self, y):
        self._yCord = y
    def updateCords(self):
        self._xCord = self._tank.getX()
        self._yCord = self._tank.getY()


class Tank_T34(Item):
    _cellSymb = "T"
    _step = 2
    _shot = 1
    _dialWrongWay = "WRONG WAY"


class Tank_Tiger(Item):
    _cellSymb = "8"
    _step = 1
    _shot = 2
    _dialWrongWay = "WRONG WAY"


class Aim (Item):
    _cellSymb = "@"
    _step = 1
    _cellSymbAfterBang = "X"

    def setCellSymb(self):
        self._cellSymb = self._cellSymbAfterBang


class Arena:
    _emptyCell = ' '
    _borderCell = '#'

    hight = 0
    width = 0
    arena = []
    typeTank = ""
    command = ""
    dialog = ""
    instruction = "The command-list:\n 'w' - up,\n 's' - down,\n 'a' - left,\n 'd' - right,\n 'q' - left-up," \
                  "\n 'e' - right-up,\n space - shoot,\n 'exit' - end game"
    shotStatus = ""

    def __init__(self, nHight, nWidth):
        self.hight = nHight+2
        self.width = nWidth+2

    def _createArena(self):
        self.arena = [0] * self.hight
        self.arena[0] = self.arena[self.hight - 1] = [self._borderCell] * self.width
        for i in range(1, (self.hight - 1)):
            self.arena[i] = [0] * self.width
            self.arena[i][0] = self.arena[i][self.width - 1] = self._borderCell
            for j in range(1, (self.width - 1)):
                self.arena[i][j] = self._emptyCell
        if (self.typeTank == "1"):
            self.tank = Tank_T34(self)
        elif(self.typeTank == "2"):
            self.tank = Tank_Tiger(self)
        self.aim = Aim(self)
        self.bang = Bang(self.tank)
        self.setDialog("ENTER THE COMMAND")

    def _updateArena(self):
        for i in range(1, (self.hight-1)):
            self.arena[i][0] = self.arena[i][self.width - 1] = self._borderCell
            for j in range(1, (self.width - 1)):
                self.arena[i][j] = self._emptyCell
        self.arena[self.tank.getY()][self.tank.getX()] = self.tank.getSymb()
        self.arena[self.aim.getY()][self.aim.getX()] = self.aim.getSymb()

    def _printArena(self):
        os.system('cls')
        print(self.instruction)
        for i in range(self.hight):
            for j in range (self.width):
                print(self.arena[i][j], end="")
            print('\n', end="")
        print("Tank cords: ", self.tank.getX(), self.tank.getY())
        print("Aim cords: ", self.aim.getX(), self.aim.getY())
        print("Shot cords: ",self.bang.getX(),self.bang.getY())
        print ("Direction: "+self.tank.getDir())
        print(self.dialog)
        #print(self.instruction)

    def _locateTank(self):
        self.tank.setX(randint(1,self.width-2))
        self.tank.setY(randint(1, self.hight-2))
        self.bang.updateCords()

    def _lokateAim(self):
        self.aim.setX(self.tank.getX())
        self.aim.setY(self.tank.getY())
        while (abs(self.aim.getX() - self.tank.getX()) <= 1):
            self.aim.setX(randint(1, self.width - 2))
        while (abs(self.aim.getY() - self.tank.getY()) <= 1):
            self.aim.setY(randint(1, self.hight - 2))

    def _getCommand(self):
        s = input()
        self.command = self.command.replace(self.command, s)

    def setDialog(self, str):
        self.dialog = self.dialog.replace(self.dialog, str)

    def setShotStatus(self):
        s = "Shot cords: "+str(self.bang.getX())+" "+str(self.bang.getY())
        self.shotStatus = self.shotStatus.replace(self.shotStatus, s)

    def _moveTank(self):
        if (self.command == 'w'):
            self.tank.move('w', self.aim)
            self.bang.updateCords()
        elif (self.command == 's'):
            self.tank.move('s', self.aim)
            self.bang.updateCords()
        elif (self.command == 'a'):
            self.tank.move('a', self.aim)
            self.bang.updateCords()
        elif (self.command == 'd'):
            self.tank.move('d', self.aim)
            self.bang.updateCords()
        elif (self.command == 'q'):
            self.tank.move('q', self.aim)
            self.bang.updateCords()
        elif (self.command == 'e'):
            self.tank.move('e', self.aim)
            self.bang.updateCords()

    def _shootTank(self):
        if (self.command == ' '):
            self.tank.shoot(self.bang)
            if (self.dialog != "WRONG SHOT"):
                self._checkShot()

    def _checkShot(self):
        if (self.aim.getX() == self.bang.getX() and self.aim.getY() == self.bang.getY()):
            self.setDialog("HIT THE TARGET!")
        else:
            self.setDialog("YOU ARE MISS")


    def _moveAim(self):
        r = randint(1,4)
        if (r == 1):
            self.aim.move('w', self.tank)
        elif (r == 2):
            self.aim.move('s', self.tank)
        elif (r == 3):
            self.aim.move('a', self.tank)
        elif (r == 4):
            self.aim.move('d', self.tank)

    def _startMenu(self):
        print("Tanki the Game (by asintsov)")
        print("Choice your Tank: ")
        print("T34 - fast, but short-range : step=2, shot=1. Button for choice: 1")
        print("Tiger - long-range, but slow: step=1, shot=2. Button for choice: 2")
        print("Input number of the Tank")
        str = input()
        self.typeTank += str
        print("LET THE FIGHT BEGIN")


    def startGame(self):
        os.system('cls')
        self._startMenu()
        os.system('cls')
        self._createArena()
        self._locateTank()
        self._lokateAim()
        self._updateArena()
        self._printArena()

    def _endGame(self):
        self.aim.setCellSymb()
        self._updateArena()
        self._printArena()
        print("YOU ARE WINNER!!!")


    def playGame(self):
        while(True):
            self._getCommand()
            if (self.command == 'exit'):
                break
            elif (self.command == 'w' or self.command == 's'
                  or self.command == 'a' or self.command == 'd'
                  or self.command == 'q' or self.command == 'e'):
                self._moveTank()
                self._updateArena()
                self._printArena()
                time.sleep(1)
                if (self.dialog != "WRONG WAY" and self.dialog != "WRONG SHOT"):
                    self._moveAim()
                    self._updateArena()
                    self._printArena()
            elif (self.command == ' '):
                self._shootTank()
                if (self.dialog == "HIT THE TARGET!"):
                    self._endGame()
                    break
                self._updateArena()
                self._printArena()
            else:
                self.setDialog("WRONG COMMAND")
                self._printArena()


a = Arena(10,10)
a.startGame()
a.playGame()
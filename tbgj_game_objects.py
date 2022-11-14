

class GameObject:
    goSymbol = "O"
    xPos = 0
    yPos = 0
    xVel = 0
    yVel = 0
    
    def __init__(self, symbol, x, y, xv, yv):
        self.setSymbol(symbol)
        self.setXPos(x)
        self.setYPos(y)
        self.setXVel(xv)
        self.setYVel(yv)
    
    # Setters
    def setSymbol(self, symbol):
        self.goSymbol = symbol
    
    def setXPos(self, x):
        self.xPos = x
     
    def setYPos(self, y):
        self.yPos = y

    def setXVel(self, xv):
        self.xVel = xv

    def setYVel(self, yv):
        self.yVel = yv

    def move(self, width, height):
        if (self.getXPos() + self.getXVel() == 0 or self.getXPos() + self.getXVel() == width):
            pass
        else:
            self.setXPos(self.getXPos() + self.getXVel())

        if (self.getYPos() + self.getYVel() == 0 or self.getYPos() + self.getYVel() == height):
            pass
        else:
            self.setYPos(self.getYPos() + self.getYVel())

    # Getters
    def toString(self):
        return self.goSymbol
    
    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getXVel(self):
        return self.xVel

    def getYVel(self):
        return self.yVel

class Player(GameObject):
    # L R U D
    orientation = ""

    def __init__(self, symbol, x, y, xv, yv, ori):
        super(Player, self).__init__(symbol, x, y, xv, yv)
        self.setOrientation(ori)

    # Setters
    def setOrientation(self, ori):
        self.orientation = ori

    # Getters
    def getOrientation(self):
        return self.orientation

class Block(GameObject):
    width = 0
    height = 0
    blockText = ""

    def __init__(self, symbol, x, y, xv, yv, width, height):
        super().__init__(symbol, x, y, xv, yv)

        self.width = width
        self.height = height

        for i in range(self.height):
            for j in range(self.width):
                # block bounds
                if(i == 0 or i == self.height - 1):
                    self.blockText += self.goSymbol
                elif(j == 0 or j == self.width - 1): 
                    self.blockText += self.goSymbol
                else:
                    self.blockText += " "
        
    # Setters
    
    # Getters
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def toString(self):
        return self.blockText


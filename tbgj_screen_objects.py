import tbgj_game_objects

class GameHeader: 
    header = ""
    name = ""
    crew = 0
    room = 0

    def __init__(self, name, crew, room):
        self.update(name, crew, room)

    # Setters
    def update(self, name, crew, room):
        self.name = name
        self.crew = crew
        self.room = room

        self.header = "NAME: " + self.name + "\n"
        self.header += "CREW: " + str(self.crew) + "\n"
        self.header += "ROOM: " + str(self.room) + "\n"

    # Getters
    def toString(self):
        return self.header

class GameMap:
    map = ""
    height = 0
    width = 0
    
    def __init__(self, width, height):
        self.setWidth(width)
        self.setHeight(height)
        self.makeMap(width, height)

    # Setters
    def makeMap(self, width, height):
        self.map = ""

        for i in range(self.height):
            for j in range(self.width - 1): # -1 since last char is \n

                # Screen bounds
                if(i == 0 or i == self.height - 1):
                    self.map += "#"
                elif(j == 0 or j == self.width - 2): # -2 since # then \n
                    self.map += "#"
                else:
                    self.map += " "

                # Empty space
                if(j == self.width - 2):
                    self.map += "\n"

    def setHeight(self, height):
        self.height = height
        self.makeMap(self.getWidth(), self.getHeight())

    def setWidth(self, width):
        self.width = width
        self.makeMap(self.getWidth(), self.getHeight())

    # Getters
    def toString(self):
        return self.map

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

class GameScreenManager:
    header = ""
    map = ""

    def __init__(self, header, map, blocks, gameObjects, player):
        self.updateGameScreen(header, map, blocks, gameObjects, player)

    # Setters
    def updateGameScreen(self, header: GameHeader, map: GameMap, blocks: list[tbgj_game_objects.Block], gameObjects: list[tbgj_game_objects.GameObject], player: tbgj_game_objects.Player):
        self.header = header.toString()
        self.map = map.toString()

        self.placeBlocks(map, blocks)
        self.placeObjects(map, gameObjects)
        self.placePlayer(map, player)

    def placeObjects(self, map: GameMap, objects: list[tbgj_game_objects.GameObject]):
        pass

    def placeBlocks(self, map:GameMap, blocks: list[tbgj_game_objects.Block]):
        mw = map.getWidth()
        mh = map.getHeight()
        
        for block in blocks:
            x = block.getXPos()
            y = block.getYPos()
            w = block.getWidth()
            h = block.getHeight()
            s = block.toString()

            for i in range(h):
                blockLine = s[i * w : (i + 1) * w]

                self.map = self.map[:((y + i) * mw + x)] + blockLine + self.map[((y + i) * mw + x) + w:]

    def placePlayer(self, map: GameMap, player: tbgj_game_objects.Player):
        mw = map.getWidth()
        mh = map.getHeight()

        x = player.getXPos()
        y = player.getYPos()
        orientation = player.getOrientation()

        # place player icon
        self.map = self.map[:(y * mw + x)] + player.toString() + self.map[(y * mw + x) + 1:]

        # place orientation arrow
        if(orientation == "U"):
            self.map = self.map[:((y - 1) * mw + x)] + "^" + self.map[((y - 1) * mw + x) + 1:]

        elif(orientation == "D"):
            self.map = self.map[:((y + 1) * mw + x)] + "v" + self.map[((y + 1) * mw + x) + 1:]

        elif(orientation == "L"):
            self.map = self.map[:(y * mw + (x - 1))] + "<" + self.map[(y * mw + (x - 1)) + 1:]

        elif(orientation == "R"):
            self.map = self.map[:(y * mw + (x + 1))] + ">" + self.map[(y * mw + (x + 1)) + 1:]

    # Getters
    def toString(self):
        return self.header + self.map

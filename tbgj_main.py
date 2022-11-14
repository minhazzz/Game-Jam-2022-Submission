import os
import time

import tbgj_screen_objects
import tbgj_game_objects
import tbgj_input

os.system('cls')


# Screen objects
name = input("WHAT IS YOUR NAME? ")
header = tbgj_screen_objects.GameHeader(name, 0, 0)
map = tbgj_screen_objects.GameMap(51, 15)

# Game objects
testBlock = tbgj_game_objects.Block("*", 5, 5, 0, 0, 10, 5)
blocks = [testBlock]
objects = list[tbgj_game_objects.GameObject]
player = tbgj_game_objects.Player("O", 1, 1, 0, 0, "D")

# IO
screenManager = tbgj_screen_objects.GameScreenManager(header, map, blocks, objects, player)
inputManager = tbgj_input.InputManager()

# game loop
while(True):
    os.system('cls')

    # Log input
    inputManager.handlePlayerInput(player)

    # Do Calculations
    player.move(map.getWidth() - 2, map.getHeight() - 1)
    screenManager.updateGameScreen(header, map, blocks, objects, player)

    # Render Screen
    print(screenManager.toString())

    time.sleep(0.03)

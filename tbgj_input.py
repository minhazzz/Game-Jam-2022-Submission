import keyboard

import tbgj_game_objects


class InputManager:
    
    def __init__(self) -> None:
        pass

    def handlePlayerInput(self, player: tbgj_game_objects.Player):
        if keyboard.is_pressed('w'):
            # print("w")
            player.setYVel(-1)
            player.setOrientation("U")

        if keyboard.is_pressed('d'):
            # print("d")
            player.setXVel(1)
            player.setOrientation("R")

        if keyboard.is_pressed('s'):
            # print("s")
            player.setYVel(1)
            player.setOrientation("D")

        if keyboard.is_pressed('a'):
            # print("a")
            player.setXVel(-1)
            player.setOrientation("L")

        if ((not keyboard.is_pressed('w')) and (not keyboard.is_pressed('s'))):
            player.setYVel(0)

        if ((not keyboard.is_pressed('a')) and (not keyboard.is_pressed('d'))):
            player.setXVel(0)
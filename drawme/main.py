#! /usr/bin/env python


def main_loop():
    # print("# main_loop #")
    pass


def launch_game(enable_joystick: bool = True):
    from game import CarpetGame
    from gamepad import Gamepad
    from pprint import pprint

    try:
        new_game = CarpetGame()   
    except Exception as e:
        print("Error")
        pprint(e)
    
    try:
        xbone = Gamepad()
        new_game.add_gamepad(xbone)
    except Exception as e:
        print("Error")
        pprint(e)
    
    new_game.main(main_loop)
    print("done")


if __name__ == "__main__":
    # blank_screen()
    # pygame_check_screens()
    launch_game()

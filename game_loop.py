import time
import states.state_manager as state_manager

game_active = True

def game_loop():
    while game_active:
        time.sleep(10)

import random
from main_menu import *

def play_dice():
    roll = random.randint(1, 6)
    print("Выпало:", roll)
main_menu()
from auth import *
from reg import *

def started_menu():
    while True:
        started_input = input ("If you first time here/want to enter to your account (R/A)")
        if started_input is 'R':
            registration()
            break
        if started_input is 'A':
            authorization()
            break
        else:
            print("Incorrect data, please try again.")
import json 

with open('user_data.json','r') as json_file:
    data = json.load(json_file)
print(data)

user = data ["users"][0]
username = user ["username"]
user_password = user ["rassword"]
print(username)
print(user_password)

import play_dice

def main_menu():
    print("Welcome to the menu!")
is_authorized = True 
if is_authorized:
    print("You are logged in. Let's start the dice roll game!")
    play_dice()
else:
    print("You are not logged in. Please log in.")

if __name__ == "__main__":
    print("\n DEBUG: Script is run in this document.")
else:
    print("Script is imported")

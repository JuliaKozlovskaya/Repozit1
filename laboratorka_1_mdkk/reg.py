from main_menu import *
from keyboard_folder import keyboard

def registration():
    print("Registration!")
    reg_name_input = input ("Enter ur name: ")
    reg_password_input = input ("Enter ur password: ")
    user["username"] = reg_name_input
    user["password"] = reg_password_input
    data["users"].append(user)
    with open ('user_data.json','w') as file_json:
        json.dump(data, json_file, intend=4)
    print(f"You have succefully registration, welcome {reg_name_input}. To continue, click Enter")
    if keyboard.wait('Enter'):
        print("Enter is pressed!")
        main_menu()
from main_menu import * 

def admin_menu():
    while True:
        print("Admin menu is succefully started!")
        print("For admin commands checks please !help!")
        admin_input = input ("Choose you wanna do: ")
        match admin_input:
            case '!delete':
                delete_user_input = input ('Which you want to delete from users? (Enter name): ')
                users = data.get('users',[])
                new_users = [user for user in users if user ['username'] != delete_user_input ]
                data['users'] = new_users
                with open ('user_data.json','w') as json_file:
                    json.dump(data, json_file, intend=4)
            case '!delete_all':
                delete_all_users_input = input ('You wipe all users account, are you sure? ')
                for data_user in data['users']:
                    updated_data = {}
                    for key, value in data_user.items():
                        if key == delete_all_users_input:
                            updated_data.update({key : value})
                        else:
                            removed_value = value
                        print(f'User {removed_value} is succefully deleted.')
                    else:
                        print('Error')
                with open ('user_data.json','w') as json_file:
                        json.dump(updated_data, json_file, indent=4)
            case '!help':
                print('In these block u can watch your commands, now available: !help, !delete, !delete_all for return to menu write 'R'')
                print('For back to register choose command !unlogin')
            case '!exit':
                print('Close the program...')
                break
            case '!unlogin':
                pass
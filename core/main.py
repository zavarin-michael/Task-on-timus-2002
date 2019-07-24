from data.users import dict_users_pass_log_in
from services.verifies import is_registered, is_logged, right_password

string = str(input())
while string != "exit":
    words = list(map(str, string.split()))
    password = ""
    command = words[0]
    user = words[1]
    if len(words) == 3:
        password = words[2]

    if command == "register":
        if is_registered(user):
            print("fail: user already exists")
        else:
            print("success: new user added")
            dict_users_pass_log_in[user] = {"password": password, "is logged": False}
    elif command == "login":
        if is_registered(user):
            if right_password(user, password):
                if is_logged(user):
                    print("fail: already logged in")
                else:
                    print("success: user logged in")
                    dict_users_pass_log_in[user]["is logged"] = True
            else:
                print("fail: incorrect password")
        else:
            print("fail: no such user")
    else:
        if is_registered(user):
            if not is_logged(user):
                print("fail: already logged out")
            else:
                print("success: user logged out")
                dict_users_pass_log_in[user]["is logged"] = False
        else:
            print("fail: no such user")


    string = str(input())


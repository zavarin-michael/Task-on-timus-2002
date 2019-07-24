from data.users import dict_users_pass_log_in



def is_registered(user):
    if user in dict_users_pass_log_in:
        return True
    else:
        return False

def is_logged(user):
    if dict_users_pass_log_in[user]["is logged"]:
        return True
    else:
        return False

def right_password(user ,password):
    if dict_users_pass_log_in[user]["password"] == password:
        return True
    else:
        return False

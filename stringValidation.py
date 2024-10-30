# Muhammad Malikj
# String Validation of Username and Password
# 10/29/2024


"""Write a function named is_valid that gets two strings arguments, username and password.

The function will return True if the username and password are valid in the system, otherwise False.

Our system contains only two valid usernames - "admin" and "user".

The valid password for username "user" is "qweasd".

For username "admin" any password is valid!"""

def is_valid(username, password):
    if username == 'user' and password == 'qweasd':
        return True
    elif username == 'admin':
        return True
    else :
        return False


bool = is_valid('user', 'qweasd')
stringBool = str(bool)
print('return value is: ', stringBool)
bool2 = is_valid('user', 'wrong')
stringBool2 = str(bool2)
print('return value is: ', stringBool2)
bool3 = is_valid('admin', 'qweasd')
stringBool3 = str(bool3)
print('return value is: ', stringBool3)

# stringBool = str(bool)
# print('return value is: ', stringBool)
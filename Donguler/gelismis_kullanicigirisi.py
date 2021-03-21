print("""
****************************************************************************************************
Welcome back! Please enter your login username and password to access SysLink Administration tool...
You have 3 attempts to login correctly.
****************************************************************************************************
""")

sys_username = "networkkid"
sys_password = "xxx_deathboi_xxx"

login_attempt = 3

while True:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if (username != sys_username and password == sys_password):
        print("Username is not in the database!")
        login_attempt -= 1
    elif (username == sys_username and password != sys_password):
        print("Password is wrong!")
        login_attempt -= 1
    elif (username != sys_username and password != sys_password):
        print("Username and password is wrong!")
        login_attempt -= 1
    else:
        print("Login successful. Welcome back {}. Administrator panel is now online!".format(sys_username))
        break

    if (login_attempt == 0):
        print("Login is unsuccessful. Please contact your supervisor!")
        break
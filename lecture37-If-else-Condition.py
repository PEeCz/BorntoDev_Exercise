username = input("Username: ")
password = input("Password: ")
if(username == "admin" and username != password):
    print("Successfully.")
else:
    print("Error Username is not a admin.")
    print("Username input and Password input not matches.")

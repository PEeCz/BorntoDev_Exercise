usernameInput = input("Username: ")
passwordInput = input("Password: ")

if usernameInput and passwordInput:
    if usernameInput != passwordInput:
        print("Login Successfully")
        print("Welcome to product inventory")
        print("1. Admin ")
        print("2. User")

        userRole = int(input(">>"))
        if userRole == 1:
            print("Item 1")
            print("Item 2")
            print("Item 3")
            print("Item 4")
        if userRole == 2:
            print("Your role is not a admin.")
    else:
        print("Username and password do not same.")
        


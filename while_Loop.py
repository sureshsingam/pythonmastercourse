actual_pwd = "python123"
enteredPwd = ""

while enteredPwd != actual_pwd:
    enteredPwd = input("Enter Password: ")
    if(enteredPwd == actual_pwd):
        print("You are logged in")
    else:
        print("Enter correct password, try again")

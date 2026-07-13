for attempt in range(1,6):

    password = input("Password: ")

    if password == "python123":
        print("Access Granted")
        break
    else:
        print("Access Denied")
        print("Attempts Left:", 5 - attempt)
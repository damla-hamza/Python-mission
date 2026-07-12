port = int(input("Enter port number: "))

if 1 <= port <= 65535:
    print("Valid Port")
else:
    print("Invalid Port")
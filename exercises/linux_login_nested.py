username = "admin"
password = "linux123"

input_username = input("Username: ")
input_password = input("Password: ")

if input_username == username:
    if input_password == password:
        print(f"Welcome! {username}")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")

print("Login Finished")
print("===== Linux User Creator =====")

number = int(input("How many users? "))

for user in range(1, number + 1):
    print("Creating user: user" + str(user))

print("All users created.")
role = input("Role: ")
namespace = input("Namespace: ")

if role == "admin":
    if namespace == "production":
        print("Full Access Granted.")
    else:
        print("Development Access Only")
else:
    print("Access denied.")

balance = 1000

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal Approved")
else:
    print("Insufficient Funds")

print("Transaction Complete")
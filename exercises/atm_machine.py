balance = 5000
pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    amount = int(input("Withdraw Amount: "))
    if amount <= balance:
        print(f"Cash Dispensed")
    else:
        print(f"Insufficient Balance")
else:
      print(f"Invalid PIN")







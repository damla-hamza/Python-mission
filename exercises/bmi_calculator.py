weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

print("\n----- Your BMI Calculation -----")
bmi = weight / (height ** 2)
print(f"Your BMI is:", round(bmi, 2))    

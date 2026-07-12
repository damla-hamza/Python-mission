print("===== Logical Operators =====")

age = 25
salary = 6000

print(f"Age: {age}")
print(f"Salary: {salary}")

print("-" * 35)

print("AND Examples")
print(age >= 18 and salary >= 5000)
print(age >= 30 and salary >= 5000)

print("-" * 35)

print("OR Examples")
print(age >= 30 or salary >= 5000)
print(age >= 30 or salary >= 7000)

print("-" * 35)

print("NOT Examples")
print(not(age >= 18))
print(not(age < 18))
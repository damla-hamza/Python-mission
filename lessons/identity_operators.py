print("===== Identity Operators =====")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a == b : {a == b}")
print(f"a is b : {a is b}")

print("-" * 30)

print(f"a == c : {a == c}")
print(f"a is c : {a is c}")

print("-" * 30)

print(f"b is not c : {b is not c}")
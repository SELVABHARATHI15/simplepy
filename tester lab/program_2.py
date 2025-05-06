# 1. Display Statement
print("--- Demonstrating Basic Programming Concepts ---")
print("This program covers display statements, data types, variables, operators, conditional statements, and loops.")

# 2. Variables and Data Types
print("\n--- Variables and Data Types ---")
# Integer variable
integer_var = 10
print(f"Variable 'integer_var' has value: {integer_var} and is of type: {type(integer_var)}")

# Float variable
float_var = 25.75
print(f"Variable 'float_var' has value: {float_var} and is of type: {type(float_var)}")

# String variable
string_var = "Hello, Python!"
print(f"Variable 'string_var' has value: '{string_var}' and is of type: {type(string_var)}")

# Boolean variable
boolean_var = True
print(f"Variable 'boolean_var' has value: {boolean_var} and is of type: {type(boolean_var)}")

# List variable (example of a collection data type)
list_var = [1, 2, 3, 4, 5]
print(f"Variable 'list_var' has value: {list_var} and is of type: {type(list_var)}")

# 3. Operators
print("\n--- Operators ---")
x = 20
y = 5

# Arithmetic Operators
print(f"x + y = {x + y} (Addition)")
print(f"x - y = {x - y} (Subtraction)")
print(f"x * y = {x * y} (Multiplication)")
print(f"x / y = {x / y} (Division)")
print(f"x % y = {x % y} (Modulo)")
print(f"x ** 2 = {x ** 2} (Exponentiation)")
print(f"x // y = {x // y} (Floor Division)")

# Comparison Operators
print(f"x > y is {x > y}")
print(f"x < y is {x < y}")
print(f"x == 20 is {x == 20}")
print(f"x != 10 is {x != 10}")

# Logical Operators
is_positive = x > 0
is_even = x % 2 == 0
print(f"is_positive and is_even is {is_positive and is_even}")
print(f"is_positive or is_even is {is_positive or is_even}")
print(f"not is_even is {not is_even}")

# 4. Conditional Statement (if-elif-else)
print("\n--- Conditional Statement ---")
temperature = 30

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's a cool day.")

# 5. Loop (for loop)
print("\n--- Loop (for loop) ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# Loop (while loop)
print("\n--- Loop (while loop) ---")
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1

print("\n--- Program Finished ---")

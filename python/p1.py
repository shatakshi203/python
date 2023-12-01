# Arithmetic operators
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
integer_division = a // b
modulo = a % b
exponentiation = a ** b

print("Arithmetic Operators:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Integer Division: {integer_division}")
print(f"Modulo: {modulo}")
print(f"Exponentiation: {exponentiation}")

# Comparison operators
x = 5
y = 7

equal = x == y
not_equal = x != y
greater_than = x > y
less_than = x < y
greater_than_equal = x >= y
less_than_equal = x <= y

print("\nComparison Operators:")
print(f"Equal: {equal}")
print(f"Not Equal: {not_equal}")
print(f"Greater Than: {greater_than}")
print(f"Less Than: {less_than}")
print(f"Greater Than or Equal To: {greater_than_equal}")
print(f"Less Than or Equal To: {less_than_equal}")

# Logical operators
p = True
q = False

logical_and = p and q
logical_or = p or q
logical_not_p = not p

print("\nLogical Operators:")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT p: {logical_not_p}")

# Bitwise operators
m = 0b1010  # Binary representation of 10
n = 0b1100  # Binary representation of 12

bitwise_and = m & n
bitwise_or = m | n
bitwise_xor = m ^ n
bitwise_not_m = ~m

print("\nBitwise Operators:")
print(f"Bitwise AND: {bin(bitwise_and)}")
print(f"Bitwise OR: {bin(bitwise_or)}")
print(f"Bitwise XOR: {bin(bitwise_xor)}")
print(f"Bitwise NOT m: {bin(bitwise_not_m)}")

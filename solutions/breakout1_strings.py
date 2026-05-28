# ============================================================
# COP 1047C - Lecture 3 Breakout 1: Strings
# ============================================================

# ----------------------------------------------------------
# PART A: Create a string with your full name and print
#         your first initial using negative indexing.
# ----------------------------------------------------------

# Create the string
full_name = "John Masseria"

# Positive indexing: first character is always index 0
print("First initial (positive index):", full_name[0])

# Negative indexing: to reach the FIRST character from the right,
# count backward the full length of the string.
# "John Masseria" has 13 characters, so index -13 reaches 'J'.
print("First initial (negative index):", full_name[-13])

# BONUS: compute the negative index dynamically using len()
# so this works for any name without counting by hand.
name_length = len(full_name)
print("First initial (dynamic negative index):", full_name[-name_length])

# Sample output:
# First initial (positive index): J
# First initial (negative index): J
# First initial (dynamic negative index): J


# ----------------------------------------------------------
# PART B: Ask for a first and last name, then print a
#         greeting showing the total character count.
# ----------------------------------------------------------

print("\n--- Part B ---")

first = input("Enter your first name: ")
last  = input("Enter your last name:  ")

full  = first + " " + last          # concatenate with a space
count = len(full)                   # total characters including the space

print(f"Hello, {full}! Your name has {count} characters.")

# Sample interaction:
# Enter your first name: Maria
# Enter your last name:  Garcia
# Hello, Maria Garcia! Your name has 12 characters.


# ----------------------------------------------------------
# PART C: Print a formatted receipt using an F-string.
# ----------------------------------------------------------

print("\n--- Part C: Receipt ---")

item          = "USB-C Cable"
quantity      = 3
price_per_unit = 12.99
total_cost    = quantity * price_per_unit

print(f"Item:           {item}")
print(f"Quantity:       {quantity}")
print(f"Price per unit: ${price_per_unit:.2f}")
print(f"Total cost:     ${total_cost:.2f}")

# Sample output:
# Item:           USB-C Cable
# Quantity:       3
# Price per unit: $12.99
# Total cost:     $38.97


# ----------------------------------------------------------
# CHALLENGE: Ask for a whole number and display it four ways:
#   1. Plain integer
#   2. Integer with comma separator
#   3. Binary representation
#   4. Hexadecimal representation
# ----------------------------------------------------------

print("\n--- Challenge: Number Formats ---")

user_input = input("Enter a whole number: ")
number = int(user_input)             # input() always returns a string — cast it!

print(f"Decimal (plain):  {number:d}")
print(f"Decimal (commas): {number:,d}")
print(f"Binary:           {number:b}")
print(f"Hex (lowercase):  {number:x}")
print(f"Hex (uppercase):  {number:X}")

# Sample interaction:
# Enter a whole number: 255
# Decimal (plain):  255
# Decimal (commas): 255
# Binary:           11111111
# Hex (lowercase):  ff
# Hex (uppercase):  FF

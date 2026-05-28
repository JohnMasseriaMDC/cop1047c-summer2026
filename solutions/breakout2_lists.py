# ============================================================
# COP 1047C - Lecture 3 Breakout 2: Lists
# ============================================================

# ----------------------------------------------------------
# Step 1: Create a list of 5 student names.
# ----------------------------------------------------------

students = ["Alice Morales", "Ben Carter", "Carlos Vega", "Diana Lin", "Evan Ruiz"]

print("Original list:")
print(students)

# ----------------------------------------------------------
# Step 2: Print the first and last name in the list.
#
# Lists use zero-based indexing, just like strings.
# The first item is index 0; the last is index -1.
# ----------------------------------------------------------

print("\nFirst student:", students[0])   # index 0
print("Last student: ", students[-1])   # negative index — last item

# ----------------------------------------------------------
# Step 3: Add a new student using append().
#
# append() adds one item to the END of the list.
# The list grows by 1.
# ----------------------------------------------------------

students.append("Fatima Hassan")

print("\nAfter append():")
print(students)
print("List now has", len(students), "students.")

# ----------------------------------------------------------
# Step 4: Remove a student by value using remove().
#
# remove() searches for the FIRST occurrence of the value
# and deletes it. The list shrinks by 1.
# ----------------------------------------------------------

students.remove("Ben Carter")

print("\nAfter remove():")
print(students)
print("List now has", len(students), "students.")

# ----------------------------------------------------------
# Sample output:
#
# Original list:
# ['Alice Morales', 'Ben Carter', 'Carlos Vega', 'Diana Lin', 'Evan Ruiz']
#
# First student: Alice Morales
# Last student:  Evan Ruiz
#
# After append():
# ['Alice Morales', 'Ben Carter', 'Carlos Vega', 'Diana Lin', 'Evan Ruiz', 'Fatima Hassan']
# List now has 6 students.
#
# After remove():
# ['Alice Morales', 'Carlos Vega', 'Diana Lin', 'Evan Ruiz', 'Fatima Hassan']
# List now has 5 students.
# ----------------------------------------------------------

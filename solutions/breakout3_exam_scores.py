# ============================================================
# COP 1047C - Lecture 3 Breakout 3: Exam Scores
# ============================================================
#
# Store a list of exam scores, then compute and print:
#   - Average score
#   - Highest score
#   - Lowest score
# ============================================================

# ----------------------------------------------------------
# Step 1: Define the list of exam scores.
# ----------------------------------------------------------

scores = [88, 92, 75, 100, 63, 84, 71, 95, 78, 90]

print("Exam scores:", scores)
print("Number of scores:", len(scores))

# ----------------------------------------------------------
# Step 2: Compute statistics.
#
# Python provides built-in functions for this:
#   max()  → returns the largest value in the list
#   min()  → returns the smallest value in the list
#   sum()  → returns the total of all values
#   len()  → returns the number of items (used to compute average)
# ----------------------------------------------------------

highest = max(scores)
lowest  = min(scores)
average = sum(scores) / len(scores)   # sum ÷ count = average

# ----------------------------------------------------------
# Step 3: Print results with F-string formatting.
#
# :.1f formats a float to 1 decimal place, which is
# appropriate for a grade average.
# ----------------------------------------------------------

print(f"\nHighest score: {highest}")
print(f"Lowest score:  {lowest}")
print(f"Average score: {average:.1f}")

# ----------------------------------------------------------
# Sample output:
#
# Exam scores: [88, 92, 75, 100, 63, 84, 71, 95, 78, 90]
# Number of scores: 10
#
# Highest score: 100
# Lowest score:  63
# Average score: 83.6
# ----------------------------------------------------------

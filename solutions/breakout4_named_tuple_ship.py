# ============================================================
# COP 1047C - Lecture 3 Breakout 4: Named Tuples — SHIP
# ============================================================
#
# Create a named tuple called SHIP with fields:
#   name, capacity, home_port, year_built
#
# Then create at least two ship instances and print details.
# ============================================================

# namedtuple lives in the 'collections' module.
# We import only what we need so we don't have to write
# collections.namedtuple every time.
from collections import namedtuple

# ----------------------------------------------------------
# Step 1: Define the SHIP named tuple "blueprint".
#
# namedtuple() takes two arguments:
#   1. The name of the tuple type (string)
#   2. A list of field names (list of strings)
# ----------------------------------------------------------

Ship = namedtuple("Ship", ["name", "capacity", "home_port", "year_built"])

# ----------------------------------------------------------
# Step 2: Create ship instances.
#
# Values are assigned positionally — same order as the
# field list above.
# ----------------------------------------------------------

wonder = Ship(
    name       = "Wonder of the Seas",
    capacity   = 6988,
    home_port  = "Port Canaveral, FL",
    year_built = 2022
)

icon = Ship(
    name       = "Icon of the Seas",
    capacity   = 7600,
    home_port  = "Miami, FL",
    year_built = 2024
)

oasis = Ship(
    name       = "Oasis of the Seas",
    capacity   = 6296,
    home_port  = "Port Canaveral, FL",
    year_built = 2009
)

# ----------------------------------------------------------
# Step 3: Print each ship's details using dot notation.
#
# Named tuples let us use field names (ship.name) instead
# of positional indexes (ship[0]), which is much more
# readable.
# ----------------------------------------------------------

print("=" * 50)
print(f"{'ROYAL CARIBBEAN FLEET SUMMARY':^50}")
print("=" * 50)

print(f"\nShip Name:  {wonder.name}")
print(f"Capacity:   {wonder.capacity:,d} passengers")
print(f"Home Port:  {wonder.home_port}")
print(f"Year Built: {wonder.year_built}")
print(f"Age:        {2026 - wonder.year_built} years")
print("-" * 50)

print(f"\nShip Name:  {icon.name}")
print(f"Capacity:   {icon.capacity:,d} passengers")
print(f"Home Port:  {icon.home_port}")
print(f"Year Built: {icon.year_built}")
print(f"Age:        {2026 - icon.year_built} years")
print("-" * 50)

print(f"\nShip Name:  {oasis.name}")
print(f"Capacity:   {oasis.capacity:,d} passengers")
print(f"Home Port:  {oasis.home_port}")
print(f"Year Built: {oasis.year_built}")
print(f"Age:        {2026 - oasis.year_built} years")
print("-" * 50)

# ----------------------------------------------------------
# Step 4: Demonstrate immutability.
#
# Tuples cannot be changed after creation. This line
# will raise a TypeError if uncommented — try it!
# ----------------------------------------------------------

# wonder.capacity = 9000   # ← TypeError: can't set attribute

# ----------------------------------------------------------
# Step 5: Demonstrate that index access still works.
#
# Named tuples are still tuples under the hood —
# you can access by position if you want to.
# ----------------------------------------------------------

print("\nAccessing by index still works:")
print(f"  icon[0] → {icon[0]}")   # name
print(f"  icon[1] → {icon[1]}")   # capacity

# ----------------------------------------------------------
# Sample output:
#
# ==================================================
#           ROYAL CARIBBEAN FLEET SUMMARY
# ==================================================
#
# Ship Name:  Wonder of the Seas
# Capacity:   6,988 passengers
# Home Port:  Port Canaveral, FL
# Year Built: 2022
# Age:        4 years
# --------------------------------------------------
#
# Ship Name:  Icon of the Seas
# Capacity:   7,600 passengers
# Home Port:  Miami, FL
# Year Built: 2024
# Age:        2 years
# --------------------------------------------------
#
# Ship Name:  Oasis of the Seas
# Capacity:   6,296 passengers
# Home Port:  Port Canaveral, FL
# Year Built: 2009
# Age:        17 years
# --------------------------------------------------
#
# Accessing by index still works:
#   icon[0] → Icon of the Seas
#   icon[1] → 7600
# ----------------------------------------------------------

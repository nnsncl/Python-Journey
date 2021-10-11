# Create a list containing the names: baby_names
baby_names = [
    'Ximena',
    'Aliza',
    'Ayden',
    'Calvin'
]

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(('Rowen', 'Sandeep'))

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)


# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
# Create a generator over the rows
generator = poker_hands.iterrows()

# Access the elements of the 2nd row
first_element = next(generator)
second_element = next(generator)
print(first_element, second_element)


# INEFICIENT WAY
data_generator = poker_hands.iterrows()

for index, values in data_generator:
  	# Check if index is odd
    if (index % 2) != 0:
      	# Sum the ranks of all the cards
        hand_sum = sum([values[1], values[3], values[5], values[7], values[9]])


# EFICIENT WAY
# Define the lambda transformation
get_square = lambda x: x ** 2

# Apply the transformation
data_sum = poker_hands.apply(get_square)
print(data_sum.head())
# import the numpy package
import numpy as np

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)


# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

# use Counter to find the top 5 most common words
top_5_words = Counter(words).most_common(5)

# display the top 5 most common words
print(top_5_words)

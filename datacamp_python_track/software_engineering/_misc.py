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


# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)


import re

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_0(text))

# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Execute the function with most complete docstring
result = rapunzel()

# Print the result
print(result)


# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)
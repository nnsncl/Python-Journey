# Writing a lambda function you already know
#Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:

# def echo_word(word1, echo):
#    """Concatenate echo copies of word1."""
#    words = word1 * echo
#    return words
#The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function.

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)


#Map() and lambda functions
#So far, you've used lambda functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.

#Recall from the video that map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:

#nums = [2, 4, 6, 8, 10]

#result = map(lambda a: a ** 2, nums)
#You can see here that a lambda function, which raises a value a to the power of 2, is passed to map() alongside a list of numbers, nums. The map object that results from the call to map() is stored in result. You will now practice the use of lambda functions with map(). For this exercise, you will map the functionality of the add_bangs() function you defined in previous exercises over a list of strings.

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)
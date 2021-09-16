# String concatenation

#String variable
#content = "a basic string"

# Methods
#print("The content is " + content)
#print("The content is {}".format(content))
#print(f"The content is {content}")

adjective = input("Adjective: ")
verbOne = input("Verb: ")
verbTwo = input("Verb: ")
partToWash = input("Require to be washed: ")

madlib = f"\
    Data Engineering requires {adjective}, and it makes me exited all the time when \
    I Think about {verbOne}. Drink water and {verbTwo} forget to wash your {partToWash}."

print(madlib)
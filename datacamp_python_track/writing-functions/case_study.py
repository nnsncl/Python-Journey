# Print the return type
# You are debugging a package that you've been working on with your friends.\
# Something weird is happening with the data being returned from one of your functions,\
# but you're not even sure which function is causing the trouble.\
# You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing,\
# and it returns something different. For instance, if you expect a function to return a numpy array, but it returns a list,\
# you can get unexpected behavior. To ensure this is not what is causing the trouble, you decide to write a decorator,\
# print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.

def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


# Counter
# You're working on a new web app, and you are curious about how many times each of the functions in it gets called.\
# So you decide to write a decorator that adds a counter to each function that you decorate.\
# You could use this information in the future to determine whether there are sections of code\
# that you could remove because they are no longer being used by the app.

def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return wrapper
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))



from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)
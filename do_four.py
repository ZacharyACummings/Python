"""
A function object is a value you can assign to a variable or pass as an 
argument. For example, do_twice is a function that takes a function object 
as an argument and calls it twice:
def do_twice(f):
    f()
    f()
Here’s an example that uses do_twice to call a function named print_spam 
twice.
def print_spam():
    print('spam')

do_twice(print_spam)
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a 
value, and calls the function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your 
script.
4. Use the modified version of do_twice to call print_twice twice, passing 
'spam' as an argument.
5. Define a new function called do_four that takes a function object and a
 value and calls the function four times, passing the value as a parameter. 
 There should be only two statements in the body of this function, not four.


"""
def do_twice(func,arg):
    """Runs a function twice.
    
    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)

def do_four(func,arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func,arg)
    do_twice(func,arg)

def print_spam():
    """Prints the word spam.
    """
    print('spam')

def print_twice(arg):
    """Prints the argument twice.
    
    arg: anything printable
    """
    print(arg)
    print(arg)

do_four(print, 'value')
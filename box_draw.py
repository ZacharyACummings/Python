"""
Note: This exercise should be done using only the statements 
and other features we have learned so far.
Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a 
comma-separated sequence of values:
print('+', '-')
By default, print advances to the next line, but you can 
override that behavior and put a space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. 
The output from the next print statement would begin on the next line.
Write a function that draws a similar grid with four rows and four columns.
"""
"""

This was to figure out how to print boxes accross

def box_accoss(x):
    print('+'+((' -'*4)+' +')*x)
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('+'+((' -'*4)+' +')*x)

This was to figure out how to print boxes in the down direction

def draw_down(y):
    print('+'+((' -'*4)+' +'))
    for i in range(y):
        box_y()
"""
def box_y(x):
    """Draws the repeatable part of the box in the y direction
    then takes the number of boxes you want in the x direction
    and multiplies it out that many times
    
    x: Number of boxes you want in the horizontal (x) direction.
    """
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('/'+(('  '*4)+' /')*x)
    print('+'+((' -'*4)+' +')*x)

def box_draw(x,y):
    """Draws the Grid taking in how many boxes you want in the x and y
    direction.

    x: Number of boxes you want in the horizontal (x) direction.
    y: Number of boxes you want in the vertical (y) direction.
    """
    print('+'+((' -'*4)+' +')*x)
    for i in range(y):
        box_y(x)

box_draw(1,5)

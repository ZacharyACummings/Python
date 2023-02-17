#Below is the code I wrote
num=0
for i in range(100):
    num += 1
    fac3 = num % 3
    fac5 = num % 5
    if fac3 == 0 and fac5 == 0:
        print('Fizz Buzz')
    elif fac3 == 0:
        print('Fizz')
    elif fac5 == 0:
        print('Buzz')
    else:
        print(num)

#Below is the code that someone else came up with that is a little better
"""
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)
"""
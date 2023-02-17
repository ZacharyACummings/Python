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


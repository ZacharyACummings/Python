G = 0
R = 0
H = 0
S = 0

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')
answer = int(input('Answer: '))
if answer == 1:
    G = G+1
    R = R+1
elif answer == 2:
    H = 1+H
    S = 1+S
else:
    print('Wrong input')

answer = 0
print('Q2) When I\'m dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
answer = int(input('Answer: '))
if answer == 1:
    H = H + 1
elif answer == 2:
    S = S + 1
elif answer == 3:
    R = R + 1
elif answer == 4:
    G = G + 1
else:
    print('Wrong input')

answer = 0
print('Q3) Which kind of instrument most pleases you ear?')
print('1) The Violin')
print('2) The Trumpet')
print('3) The Piano')
print('4) The Drums')
answer = int(input('Answer: '))
if answer == 1:
    S = S + 1
elif answer == 2:
    H = H + 1
elif answer == 3:
    R = R + 1
elif answer == 4:
    G = G + 1
else:
    print('Wrong input')
1

if G > R & G > H & G > S:
    print('You belong to the House of Gryffindor')
elif R > G & R > H & R > S:
    print('You belong to the House of Ravenclaw')
elif H > G & H > R & H > S:
    print('You belong to the House of Hufflepuff')
elif S > G & S > H & S > R:
    print('You belong to the House of Slytherin')
elif G > H & G == R:
    print('You belong to both the House of Gryffindor and House of Ravenclaw')
elif H > G & H == S:
    print('You belong to both the House of Hufflepuff and House Slytherin')
elif H == G == R == S:
    print('You are the chosen one. You belong to every house.')
else:
    print('Can not sort')

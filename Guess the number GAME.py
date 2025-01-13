import random
n = random.randrange(0,10)
f = 'no'
while f == 'no' :
    a = int(input('Enter number : '))
    if a > n :
        print('>')
    elif a < n :
        print('<')
    if a == n :
        print('____________')
        print('Your guess is correct')
        f = 'yes'
print('____________')
import random

from pip._vendor.distlib.compat import raw_input

num = random.randint(0,100)
while True:
    try:
        guess = int(raw_input('Enter 1-100'))
    except ValueError as e:
        print('Enter 1-100')
        continue
    if guess > num:
        print('please input a smaller number than ',guess)
    elif guess < num:
        print('please input a bigger number than ',guess)
    else:
        print('Right, Game Over')
        break
    print('\n')

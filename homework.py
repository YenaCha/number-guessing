import random
r = random.randint(1,10)
chances = 3
while(chances>0):
    guess = int(input('Guess the number : '))
    if(guess == r):
        print('Congratulations, you are correct')
        break
    elif(guess>r):
        print('Your guess is too big')
    else:
        print('Your guess is too small')
    chances = chances-1
if(chances == 0):
    print('You lost. The actual number is : '+str(r))
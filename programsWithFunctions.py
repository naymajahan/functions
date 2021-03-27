#### fibonacchi sequence
## 0,1,1,2,3,5,8.............
## Solution

def fibonacchi(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)

        for i in range(1,n):
            z = x+y
            x = y
            y = z
            print(z)


fibonacchi(4)



### Guessing Age
## Secret Age
# Solution


import random as r
secretAge = r.randint(1,10)
flag = False

def gameFunc(guessedAge,secret):
    if guessedAge < secret:
        return "Too Low"
    elif guessedAge > secret:
        return 'Too High'
    else:
        return 'CORRECT!'

for i in range(1,6):
    print('Take a Guess, You Have '+str(6-i)+ 'guess Left')
    guess = input()
    if gameFunc(int(guess), secretAge) == "CORRECT!":
        print('YOU WON THE GAME')
        flag = True
        break

if not flag:
    print('You lose The Game')


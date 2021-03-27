## Write a Function to Check a Number is Odd or Even
### SOLUTION ###SOLUTION #### SOLUTION
print('Input any Number')
number = input()
digit = float(number)

if digit % 2 == 0:
    print('This is an Even Number')
else:
    print("This is an Odd Number")



### Write a Function to Check If a Number is Prime or Not.
#### SOLUTION #### SOLUTION #### SOLUTION



import math

print('Input a Number')
number = int(input())

def checkPrime(number):
    count = 0
    for i in range(2,math.floor(math.sqrt(number))+1):
        if number % i == 0:
            print('The Number is  not Prime')
            break
        count = count+1
    if count+2 == math.floor(math.sqrt(number))+1:
        print('The Number is Prime')


checkPrime(number)




## Write an Area() function,That Takes An User Input, then corrospondingly selects which area to print.
## Inside the Choice, The User is Again Asked to take the req input.
### SOLUTION ### SOLUTION ##### SOLUTION


def areaFunc():
    print('Enter The Shape To Find The Area:-')
    shape = input()

    if shape == 'CIRCLE':
        print('Please Enter The Radius')
        r = float(input())
        area = 3.1416*r*r
        print('The Area of Circle is ')
        print(area)
    elif shape == 'RECTANGLE':
        print("Please Enter the Length")
        l = float(input())
        print('Please Enter the Width')
        w = float(input())
        area = l*w
        print('The Area of the Rectangle is ')
        print(area)
    elif shape == 'TRIANGLE':
        print('please Enter The Height of the Triangle')
        h = float(input())
        print('Please Enter The Base of the Triangle')
        b = float(input())
        area = 0.5*(h*b)
        print('The Area of the Triangle is ')
        print(area)

    elif shape == 'SQUARE':
        print("Please Enter The Length of The Square")
        L = float(input())
        area = L*L
        print('The Area of The Square is ')
        print(area)

    elif shape == "Trapezium":
        print('Please Enter The Length of Side-1:')
        sa = float(input())
        print('Please Enter The Length of Side-2:')
        sb = float(input())
        print('Please Enter The Height of The Trapezium')
        h = float(input())
        area = 0.5*(sa+sb)*h
        print("The Area of The Trapezium is ")
        print(area)
    else:
        print('Please Enter Any of This 5 Shape- 1.CIRCLE, 2.RECTANGLE, 3.TRIANGLE, 4.SQUARE, 5.TRAPEZIUM')


areaFunc()



### HCF(Highest Common Factor Using for Loop) Between two Numbers
### SOLUTION ### SOLUTION


def commonFactor(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a

    for i in range(1,smaller+1):
        if a % i == 0 and b % i == 0:
            ans = i
            print(ans)

commonFactor(15,30)



### Write a Small Function to Depict a Rock-Paper-Sciaaors Game.
### Your Function Should take two inputs and should give us the  winner based on a certain condition.
### SOLUTION ##SOLUTION ### SOLUTION


print('What do You Want To Chose? rock, paper or scissors?')
p1 = input()
print('What do You Want To Chose? rock, paper or scissors?')
p2 = input()

def game(a,b):
    if a == b:
        return "It's a tie!"
    elif a == 'rock':
        if b == 'scissors':
            return "Rock Beats Scissors!"
        else:
            return "paper Beats Rock!"
    elif a == 'scissors':
        if b == "paper":
            return "Scissors beat Paper"
        else:
            return "Rock Beat Scissors"
    elif a == "paper":
        if b == 'rock':
            return "Paper Beats Rock"
        else:
            return "Scissors Beat Paper"
    else:
        return "You Have not Entered rock,paper or scissors."

print(game(p1,p2))



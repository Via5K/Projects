#this is a guess a number game
def YourAttempts(name):
    print('Hey',name,'What do you think, In how many attempts can you guess the number i am thinking?', end='')
    numberOfGuess= int(input())
    if numberOfGuess > 3 and numberOfGuess < 20:
        return(numberOfGuess)
    else:
        guessing(numberOfGuess,name)
    
#Yes Or No
def YesOrNo(decission,name):
    if(decission == 'N' or decission == 'n'):
        #numberOfGuess=3
        pass
    elif(decission == 'Y' or decission == 'y'):
        #goto function and ask for number of guesses again
        YourAttempts(name)
    else:
        print('Please Enter a valid Choice from Y and N')
        #goto guessing function again
        decission0 = input()
        decission = decission0[0]
        YesOrNo(decission,name)

def PlayAgain():
    print('Do you want to Play Again?\nPress Y for YES\nPress N for No')
    Play_Again0=input()
    Play_Again = Play_Again0[0]
    if(Play_Again=='y' or Play_Again=='Y'):
        startgame() #playagain 
    else:
        sys.exit() #program exits
        
def Working(secretNumber,numberOfGuess):
    for i in range(0,numberOfGuess,1):
        secretNumberGuess = int(input('Enter The number i am thinking '))
        if(secretNumberGuess<secretNumber):
            print('You Guessed a low number.\nTry Again!')
            #Goes to loop again
            i=i+1
        elif(secretNumberGuess>secretNumber):
            print('You Guessed a high number.\nTry Again!')
            #Goes to loop again
            i=i+1
        elif(secretNumberGuess==secretNumber):
            print('Hurray!! You got it right, I also guessed the number',secretNumber,'\nYou got it right at',i+1,'Number of attempts')
            #Chances over OR when user gets number right game ends.
            break
    else:
        print('I was thinking of the number - ',secretNumber)
        #if user doent gets right number then this shows what was the number game was guessing.


#Guessing Function-
def guessing(numberOfGuess,name):
    if numberOfGuess<3: #used so that user cannot enter value less than 3
        print('Ooops!', name, 'I will allot you a minimum of 3 attempts')
        numberOfGuess=3 #assigned value = 3 for number of attemps.
        decission0 = input('Do you want to change my decission? \nPress Y for Yes\nPress N for No ')
        decission = decission0[0]
        YesOrNo(decission,name) #Function to check wther the person want to change his decission or not?
        
    elif numberOfGuess>20 :
        print('Buzzy Trick',name,'Thats not a good gaming spirit. So, i am alloting you a maximum of 20 attempts')
        numberOfGuess=20
        decission0 = input('Do you want to change my decission? \nPress Y for Yes\nPress N for No ')
        decission = decission0[0]
        YesOrNo(decission,name) #Function to check wther the person want to change his decission or not?

    else:
        print('Okay, Let us start the game\n')
        #everything goes fine then user proceeds to the game.


def startgame(): 
    print("Hello, What is your name: ")
    name= input()
    print('Hello',name,'I am thinking of a number between 1-50')
    secretNumber = random.randint(1,50) #this guesses a random number.
    numberOfGuess=0 #i have given here that minimum number of guess = 0 
    numberOfGuess = YourAttempts(name)
    guessing(numberOfGuess,name) 
    Working(secretNumber,numberOfGuess)        #working Function
    PlayAgain()

import random
import sys
startgame()
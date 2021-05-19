#RollingDice Program....

import random

def Rolling():
	number = random.randint(1,6)
	return number

def Dice(FaceValue):
	if FaceValue==1:
		print(""" 
		 - - -
		|     |
		|  *  |
		|     |
		 - - -
		""")
	elif FaceValue ==2:
		print("""
		 - - -
		|*    |
		|     |
		|   * |
		 - - -
		""")
	elif FaceValue ==3:
		print("""
		 - - -
		|*    |
		|  *  |
		|    *|
		 - - -
		""")
	elif FaceValue ==4:
		print("""
		 - - -
		|*   *|
		|     |
		|*   *|
		 - - -
		""")
	elif FaceValue ==5:
		print("""
		 - - -
		|*   *|
		|  *  |
		|*   *|
		 - - -
		""")
	else:
		print("""
		 - - -
		|*   *|
		|*   *|
		|*   *|
		 - - -
		""")
		
		
#MAIN PROGRAM

print("Welcome To Rolling Dice\n\n")
while True:
	FaceValue= Rolling()
	Dice(FaceValue)
	PlayAgain = input('Do You Wanna Roll Again? (Y/N): ')
	if PlayAgain == 'Y' or PlayAgain == 'Yes' or PlayAgain =='yes' or PlayAgain =='YES' or PlayAgain == 'y':
		continue
	elif PlayAgain[0] =='n' or PlayAgain[0] =='N' :
		break
	else:
		print("Something Went Wrong In My Mind.. Let's Restart...")
		continue
	



"""
THEORY / EXAMPLE / EXPLANATION

Create this: 

 - - -
|*    |
|     |
|   * |
 - - -

"""
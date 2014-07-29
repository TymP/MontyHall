#Script: Monty hall problem
from random import randint

#Set change boolean
Change = True
#The possible combinations of three doors. False = donkey, True = car.

#initialise score keepers
tries = 0
changeAndWin = 0
win=0

#Start game loop.
while tries<1000:

    #CAREFUL THESE NEED TO BE REINITIALISED ON EACH ITERATION
    #when you del remainingDoors[index], that  points ot the original array
    doors1 = [True, False, False]
    doors2 = [False,True,False]
    doors3 = [False, False, True]
    possibleDoors = [doors1, doors2, doors3]
    print('possible doors:')
    print(possibleDoors)

    #Alternate changing mind and not changing mind
    if tries%2 ==0:
        change = True
    else:
        change = False
        
    #Set the stage
    remainingDoors = possibleDoors[randint(0,2)]
    print('initial doors: ')
    print(remainingDoors)
    choiceIndex = randint(0,2)
    print('choice index: ', choiceIndex)
    choice = remainingDoors.pop(choiceIndex)
    print('choice: ',choice)
    print("removing choice")
    print('doors: ', remainingDoors)
    print("change: ", change)
    
    if change:
        for i in range(len(remainingDoors)):
            if remainingDoors[i]==False:
                del remainingDoors[i]#THEBUG
                break
        choice = remainingDoors[0]
        
    tries +=1

    if(choice == True):
        print('Player won!')
        win+=1
    else:
        print('Player lose')
    if(change and choice):
        changeAndWin +=1
    print('tries: ',tries)
    print('win: ', win)
    print(" ")
    print(' ')

print('change and win:', changeAndWin)
print('changeswins/wins:',changeAndWin/win)
if changeAndWin>win/2:
    print('Monty Hall conclusion: you should change your mind')
    
        
    
    
    



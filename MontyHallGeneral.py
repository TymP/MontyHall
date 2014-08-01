#Script: Monty hall general case
from random import randint

numberOfDoors = 4

#initialise score keepers
tries = 0
changeAndWin = 0
win=0

#Start game loop.
while tries<10:

    #CAREFUL THESE NEED TO BE REINITIALISED ON EACH ITERATION
    #when you del remainingDoors[index], that  points ot the original array
    
    possibleDoors = [[False]*numberOfDoors]*numberOfDoors
    for i in range(numberOfDoors):
        possibleDoors[i][i] = True

    #Alternate changing mind and not changing mind
    if tries%2 ==0:
        change = True
        print("Player changed mind")
    else:
        change = False
        
    #Set the stage
    remainingDoors = possibleDoors[randint(0,numberOfDoors-1)]
    choiceIndex = randint(0,numberOfDoors-1)
    choice = remainingDoors.pop(choiceIndex)

    #If player changes mind:
    if change:
        #Reveal a goat:
        for i in range(len(remainingDoors)):
            if remainingDoors[i]==False: #it's a goat
                del remainingDoors[i]#Remove it: it's no longer a choice
                break
        choice = remainingDoors[randint(0,numberOfDoors-1)]
        
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

#Analysis
print('change and win:', changeAndWin)
print('changeswins/wins:',changeAndWin/win)
if changeAndWin>win/2:
    print('Monty Hall conclusion: you should change your mind')
    
        
    
    
    



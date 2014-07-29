#Script: Monty hall general case
from random import randint

#General case: initialise list for number of doors
numberOfDoors = 4
possibleDoors = [[False]*numberOfDoors]*numberOfDoors
for i in range(numberOfDoors):
    possibleDoors[i][i] = True

#initialise score keepers
tries = 0
changeAndWin = 0
win=0

#Start game loop.
while tries<10:

    #CAREFUL THESE NEED TO BE REINITIALISED ON EACH ITERATION
    #when you del remainingDoors[index], that  points ot the original array
    doors1 = [True, False, False]
    doors2 = [False,True,False]
    doors3 = [False, False, True]
    possibleDoors = [doors1, doors2, doors3]

    #Alternate changing mind and not changing mind
    if tries%2 ==0:
        change = True
        print("Player changed mind")
    else:
        change = False
        
    #Set the stage
    remainingDoors = possibleDoors[randint(0,2)]
    choiceIndex = randint(0,2)
    choice = remainingDoors.pop(choiceIndex)

    #If player changes mind:
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

#Analysis
print('change and win:', changeAndWin)
print('changeswins/wins:',changeAndWin/win)
if changeAndWin>win/2:
    print('Monty Hall conclusion: you should change your mind')
    
        
    
    
    



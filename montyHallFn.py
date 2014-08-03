def montyHallFn(numberOfDoors):
    from random import randint
    NUMBER_OF_DOORS= numberOfDoors
    ITERATIONS = 100000

    #initialise score keepers
    tries = 0
    changeAndWin = 0
    stayAndWin =0
    changes=0
    stays=0
    shouldChange = True

    #Game loop.
    while tries<ITERATIONS:
        #Create array of possible door arrays of given length
        #bools are immutable, so have to be initialised as seperate objects
        possibleDoors = [[False for i in range(NUMBER_OF_DOORS)]for j in range(NUMBER_OF_DOORS)]
        #Put a car behind a different door in each array.
        for i in range(NUMBER_OF_DOORS):
            possibleDoors[i][i] = True
        #Alternate changing mind and not changing mind
        if(tries%2 ==0):
            change = True
            changes+=1
        else:
            change = False
            stays+=1
        
        #Set the stage
        remainingDoors = possibleDoors[randint(0,NUMBER_OF_DOORS-1)]
        choiceIndex = randint(0,NUMBER_OF_DOORS-1)
        choice = remainingDoors.pop(choiceIndex)

        #If player changes mind:
        if change:
            #Reveal a goat:
            for i in range(len(remainingDoors)):
                if not remainingDoors[i]: #it's a goat
                    del remainingDoors[i]#Remove it: it's no longer a choice
                    break
            #Reassign choice to a random remaining door
            choice = remainingDoors[randint(0,len(remainingDoors)-1)]
        
        tries +=1

        if(change and choice):
            changeAndWin +=1
        if(not change and choice):
            stayAndWin +=1
       
    #Analysis
    PwinGchange=changeAndWin/changes
    PwinGstay = stayAndWin/stays
    if(PwinGchange<=PwinGstay):
        shouldChange=False

    return shouldChange

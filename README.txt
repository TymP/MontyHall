These scripts iteratively analyse the Monty Hall Problem. 

The Monty Hall Problem:

On a game show, you are asked to choose one of three doors. You will win whatever is behind the door you choose.
Behind one door is a car and behind the other two, goats.

You make a random choice of one of the three doors. But before opening your chosen door, the host opens one of the two remaining doors, revealing a goat.
He then asks you if you want to change your original choice.

Will changing give you a better chance of winning the car?

Assumptions:
-There is always only one car, the remaining doors contain goats.
-The host always reveals a goat.
-The player makes a first chocie at random.
-The positions of the goats and car are random.

The script distills the problem down to an array of booleans representing the various doors.

True indicates that the door contains a car, while False means it contains a goat. 
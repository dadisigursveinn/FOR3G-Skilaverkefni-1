from random import randint
array = [0, 0, 0, 0, 0]
count = 0
playing = 0
win = 0
while count < 5:
    randomNumber = randint(0, 8)
    if randomNumber not in array:
        array[count] = randomNumber
        count += 1
for x in range(5):
    array[x] = str(array[x])
print "computer has generated numbers now its your time to guess the sequence"
while playing <= 7 and win == 0:
    rightPlace = 0
    rightNum = 0
    guess = list(str(input()))
    for x in range(5):
        if guess[x] == array[x]:
            rightPlace += 1
        for y in range(5):
            if guess[x] == array[y]:
                rightNum += 1
    print "you had " + str(rightNum) + " right numbers in " + str(rightPlace) + " places right"
    if rightNum == 5 and rightPlace == 5:
        win = 1
    playing += 1
print "\nthe sequence was " + str(array)
print "your guess was   " + str(guess)
rightPlace = 0
rightNum = 0
for x in range(5):
    if array[x] == guess[x]:
        rightPlace += 1
    for y in range(5):
        if guess[x] == array[y]:
           rightNum += 1
print "you had " + str(rightNum) + " right numbers in " + str(rightPlace) + " places right"
raw_input("")





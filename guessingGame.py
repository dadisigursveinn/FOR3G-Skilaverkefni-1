from random import randint
guess = 0
win = 0
score = [1280, 640, 320, 160, 80, 40, 20, 10]
randomInt = randint(1, 100)
print "The computer has generated a number between 1 and 100 you have 8 guesses"
while guess < 8 and win == 0:
    guess += 1
    userGuess = input("your guess")
    if userGuess == randomInt:
        win = 1
    elif userGuess > randomInt:
        print "your guess was to high"
    else:
        print "your guess was to low"
if win == 1:
    print "you won and got " + str(score[guess-1]) + " points"
    print "winning number " + str(randomInt)
else:
    print "you lost"
    print "winning number " + str(randomInt)
raw_input("")

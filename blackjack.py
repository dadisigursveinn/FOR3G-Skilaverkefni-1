from random import randint
print "There is an infinite amount of decks aces are worth 11, kings, queens and jacks are worth 10"
playing = "yes"
cWin = 0
pWin = 0
tie = 0
points = 50000
print "you have " + str(points) + " points"
while playing == "yes" and points >= 500:
    player = 0
    computer = 0
    bet = 0
    while bet < 500 and bet >= points:
        bet = input("What do you want to bet min 500\n")
    points -= bet
    give = "yes"
    print "Bet " + str(bet)
    while give == "yes":
        pCard = randint(1, 11)
        player += pCard
        if player > 21:
            give = "no"
            break
        print "you got " + str(pCard) + " you have " + str(player)
        give = raw_input("Do you want to get another card yes/no?\n")
    while computer < 17:
        cCard = randint(1, 11)
        computer += cCard
    if computer == player:
        tie += 1
        print "tie both had " + str(computer)
    elif computer > 21:
        pWin += 1
        points += (bet*2)
        print "player won with " + str(player) + " computer had " + str(computer)
    elif player > 21:
        cWin += 1
    elif computer < player:
        pWin += 1
        points += (bet*2)
        print "player won with " + str(player) + " computer had " + str(computer)
    elif player < computer:
        cWin += 1
        print "computer won with " + str(computer) + " you had " + str(player)
    print "you now have " + str(points) + " points"
    if points > 500:
        playing = raw_input("Do you want to play again yes/no?")
print "Computer won " + str(cWin) + " times. Player won " + str(pWin) + " times. There were " + str(tie) + " ties."
raw_input("")

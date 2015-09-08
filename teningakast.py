from random import randint
summaTolvunnar = 0
for x in range(1, 7):
    summaTolvunnar += randint(1,6)
playing = 0
attemt = 0
enter = 0
while playing == 0 and attemt < 3:
    attemt += 1
    summaLeikmanns = 0
    for x in range(1, 7):
        raw_input("Press enter to roll dice " + str(x))
        summaLeikmanns += randint(1, 6)
        print "you now have " + str(summaLeikmanns) + "\n"
    if attemt < 3:
        playing = input("press 1 to check if you won or 0 to try again\n")
print "-------------------------\ncomputer got " + str(summaTolvunnar)
print "you got " + str(summaLeikmanns)
if summaLeikmanns > summaTolvunnar:
    print "you won"
elif summaLeikmanns == summaTolvunnar:
    print "tie"
else:
    print "computer won"
print "-------------------------"
raw_input("")

print "The result of the dice roll is", random.randint

print "How many dice would you like to roll? Also, how many sides would you like for each dice to have?"
dice = raw_input()
sides = raw_input()
print random.randint(1,sides)
print random.randint(1,dice)

# The name of the agent. This is a REQUIRED STRING.
name = 'Lorenz'

# You can create variables. They won't be shared or visible by the other agents. They are persistent between matches, not between competitions.
# Sometimes, you might want to clear them between matches. You'll know a new match has started by reading the info passed through the 'data' parameter.
previousChoice = None

# The turn function. This FUNCTION is REQUIRED. It has one passed parameter: the 'data' parameter. To see what's in it, just print the contents to the console.
# The turn function has a RETURN of type STRING. There are four options: 'NORTH', 'EAST', 'SOUTH' and 'WEST'.
# Make sure you always return one of these (no typos), as failing to do so will result in a match loss...
# Also note: if a match hangs/ breaks while the wrapper was working on your turn, you will lose that match!
def turn(data):
	# You'll have to 'global' the persistent variables.
	# Non-persistent vars can be created in function.
	global previousChoice
	
	# When using imports, make sure they'll run on my computer. Please, ask me to do a test-run BEFORE submitting.
	import random
	
	options = ['NORTH', 'EAST', 'SOUTH', 'WEST']
	oppositeOfPreviousChoice = None
	if previousChoice == 'NORTH':
	  oppositeOfPreviousChoice = 'SOUTH'
	elif previousChoice == 'EAST':
	  oppositeOfPreviousChoice = 'WEST'
	elif previousChoice == 'SOUTH':
	  oppositeOfPreviousChoice = 'NORTH'
	elif previousChoice == 'WEST':
	  oppositeOfPreviousChoice = 'EAST'
	choice = oppositeOfPreviousChoice
	while choice is oppositeOfPreviousChoice:
		choice = options[random.randint(0, len(options) - 1)]
	previousChoice = choice
	return choice

"""
Some notes on the Lorenz agent:
The Lorenz agent is based on the random system, which means that its first turn (or any turn it doesn't really know what to do) will be chosen at random.
If you would like your agent to win more than about 45% - 55% of the matches played; do not use ANY random functions, unless you use them to make it harder for your opponents to figure out your tactics, but I guess we won't see much of that...
Lorenz exemplifies the use of persistent variables, by remembering it's previous direction and thus not bumping into its own head. (Hey, it's something!)
Don't forget to take a look at the other agents; Menno and Saskia!
Please note:
I know the names of the agents given by me as examples may sound somewhat familiar. This is completely coincidental, I swear! (*ahum*)
All the examples are just that: examples. Lorenz = persistent variables, Menno = data parameter and Saskia = basic fitness.
They are not really made to play against each other...
It is up to you and your teammates (if any) to combine the things shown in these examples, and to come up with creative ways to create an agent that will amaze.
Best of luck,
~ Scriblink
& TheYsconator
"""
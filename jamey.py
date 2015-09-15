# The name of the agent. This is a REQUIRED STRING.
name = 'Jamey'

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
	
	width = data.world_width_current
	height = data.world_height_current

	board = world_data

	player = {
		'x' = data.agent[0].position.x,
		'y' = data.agent[0].position.y
	}

	enemy = {
		'x' = data.agent[1].position.x,
		'y' = data.agent[1].position.y
	}


	return choice

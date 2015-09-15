# The name of the agent. This is a REQUIRED STRING.
name = 'Team Red'

import random

globs = {
	'data': None
}

# The turn function. This FUNCTION is REQUIRED. It has one passed parameter: the 'data' parameter. To see what's in it, just print the contents to the console.
# The turn function has a RETURN of type STRING. There are four options: 'NORTH', 'EAST', 'SOUTH' and 'WEST'.
# Make sure you always return one of these (no typos), as failing to do so will result in a match loss...
# Also note: if a match hangs/ breaks while the wrapper was working on your turn, you will lose that match!
def turn(data):
	global globs

	globs['data'] = data

	x = globs['data']['agents'][0]['position']['x']
	y = globs['data']['agents'][0]['position']['y']

	viable = viableDirections(x, y)

	choice = viable[random.randint(0, len(viable)-1)]
	
	return choice

def fill():
	global globs


def viableDirections(x, y):
	global globs

	viable = [];

	width = globs['data']['world_width_current']
	height = globs['data']['world_height_current']

	board = globs['data']['world_data']

	if (y != 0):
		if(board[y-1][x]['agentID'] == None):
			viable.append('NORTH')
	if (x != width-1):
		if(board[y][x+1]['agentID'] == None):
			viable.append('EAST')
	if (y != height-1):
		if(board[y+1][x]['agentID'] == None):
			viable.append('SOUTH')
	if (x != 0):
		if(board[y][x-1]['agentID'] == None):
			viable.append('WEST')

	return viable

def detectLock():
	return None

def determineChoice():
	return None

def startingPosition():
	return None
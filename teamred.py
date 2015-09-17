# The name of the agent. This is a REQUIRED STRING.
name = 'Team Red'

import random
import time

globs = {
	'data': None
}

# The turn function. This FUNCTION is REQUIRED. It has one passed parameter: the 'data' parameter. To see what's in it, just print the contents to the console.
# The turn function has a RETURN of type STRING. There are four options: 'NORTH', 'EAST', 'SOUTH' and 'WEST'.
# Make sure you always return one of these (no typos), as failing to do so will result in a match loss...
# Also note: if a match hangs/ breaks while the wrapper was working on your turn, you will lose that match!
def turn(data):
	global globs

	start_time = time.time()
	globs['data'] = data

	x = globs['data']['agents'][0]['position']['x']
	y = globs['data']['agents'][0]['position']['y']

	

	print (detectLock())
	viable = viableDirections(x, y)

	choice = viable[random.randint(0, len(viable)-1)] if len(viable) > 0 else 'SUDOKU'

	end_time = time.time() - start_time

	print ('time elapssed: ' + str(end_time))
	return choice

def fill():
	global globs


def viableDirections(x, y):
	global globs

	viable = []

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
	m = globs['data']['world_data']
	w,h = len(m[0]),len(m)
	sx,sy = globs['data']['agents'][0]['position']['x'],globs['data']['agents'][0]['position']['y']
	ex,ey = globs['data']['agents'][1]['position']['x'],globs['data']['agents'][1]['position']['y']
	#[parent node, x, y,g,f]
	node = [None,sx,sy,0,abs(ex-sx)+abs(ey-sy)] 
	closeList = [node]
	createdList = {}
	createdList[sy*w+sx] = node
	k=0
	while(closeList):
		node = closeList.pop(0)
		x = node[1]
		y = node[2]
		l = node[3]+1
		k+=1
		#find neighbours 
		#make the path not too strange
		if k|1:
			neighbours = ((x,y+1),(x,y-1),(x+1,y),(x-1,y))
		else:
			neighbours = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
		for nx,ny in neighbours:
			if nx==ex and ny==ey:
				path = [(ex,ey)]
				while node:
					path.append((node[1],node[2]))
					node = node[0]
				return False            
			if 0<=nx<w and 0<=ny<h and m[ny][nx]['agentID']==None:
				if ny*w+nx not in createdList:
					nn = (node,nx,ny,l,l+abs(nx-ex)+abs(ny-ey))
					createdList[ny*w+nx] = nn
					#adding to closelist ,using binary heap
					nni = len(closeList)
					closeList.append(nn)
					while nni:
						i = (nni-1)>>1
						if closeList[i][4]>nn[4]:
							closeList[i],closeList[nni] = nn,closeList[i]
							nni = i
						else:
							break


	return True

def determineChoice():
	

	return None

def startingPosition():
	strat = ['fill', 'cutoff', 'survive']

	return None

    
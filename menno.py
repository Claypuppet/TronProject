# The name of the agent. This is a REQUIRED STRING.
name = 'Menno'

# The turn function. This FUNCTION is REQUIRED. It has one passed parameter: the 'data' parameter. To see what's in it, just print the contents to the console.
# The turn function has a RETURN of type STRING. There are four options: 'NORTH', 'EAST', 'SOUTH' and 'WEST'.
# Make sure you always return one of these (no typos), as failing to do so will result in a match loss...
# Also note: if a match hangs/ breaks while the wrapper was working on your turn, you will lose that match!

globs = {
  'data': None,
  'match_previous': 0,
}

def turn(data):
  # We global the globs variable. See the Lorenz agent for more information.
  global globs
  
  # Let's make data global:
  globs['data'] = data
  
  # If globs['match_previous'] still holds the value 0 (you'll see when we change it in a moment), it means we haven't had any turn yet.
  # Let's init some things, like figuring out our agentID.
  if globs['match_previous'] == 0:
    getAndStoreOurID()
    # So now our agentID is stored in globs['id_ours']
  
    # Now we can figure out the ID of our opponent...
    figureOutAndStoreOpponentID()
    # ...which is now stored in globs['id_theirs']
  
  # If a new match has started, we might want to clear some variables...
  if globs['data']['match_current'] != globs['match_previous']:
    # ...so let's do that in a function.
    newMatch()
    
  # Menno is going to copy what its opponent did the turn before.
  # This means that it doesn't know what to do the first turn...
  # To solve this, we'll just go north every first turn. ^_^ Problem solving; I like it.
  direction = 'NORTH'
  if globs['data']['turn_current'] == 1:
    # Let's store the position of our opponent, to make it easier to determine it's previous direction.
    # Thinking ahead: +1
    storePositionOfOpponent()
    return direction
  
  else:
    # Now we need to figure out what direction our opponent went the turn before...
    direction = determineDirectionOfOpponentPreviousTurn() # Oh names, you so silly.
    storePositionOfOpponent()
    return direction

# Gets and stores the ID of this agent.
def getAndStoreOurID():
  global globs
  global name
  
  for agent in globs['data']['agents']:
    if agent['name'] == name:
      globs['id_ours'] = agent['id']
  return None
  
# Figures out the ID of the opponent, and stores it.
def figureOutAndStoreOpponentID():
  global globs
  
  if globs['id_ours'] == 0:
    globs['id_theirs'] = 1
  else:
    globs['id_theirs'] = 0
  return None

# Used to clean up stuff at the beginning of every match.
def newMatch():
  global globs
  
  globs['match_previous'] = globs['data']['match_current']
  # Clean up more stuff here, maybe?
  return None
  
# Stores the position of the opponent.
def storePositionOfOpponent():
  global globs
  
  globs['position_opp_previous'] = globs['data']['agents'][globs['id_theirs']]['position']
  return None
  
# Determines the direction of the opponent from the previous turn.
def determineDirectionOfOpponentPreviousTurn():
  global globs
  
  prev_pos = globs['position_opp_previous']
  new_pos = globs['data']['agents'][globs['id_theirs']]['position']
  delta_x = new_pos['x'] - prev_pos['x']
  delta_y = new_pos['y'] - prev_pos['y']
  if (delta_x == 0) and (delta_y == -1):
    return 'NORTH'
  elif (delta_x == 1) and (delta_y == 0):
    return 'EAST'
  elif (delta_x == 0) and (delta_y == 1):
    return 'SOUTH'
  else:
    return 'WEST'

"""
Some notes on the Menno agent:
The Menno agent exemplifies how you're able to get more information from the data parameter than you might think. First, it shows how to know the index of your agent, then it shows what direction your opponent chose the turn before. Menno will choose that direction. For information about the persistent variables, please see the Lorenz agent.
What's not shown in this example, is that you can also determine the direction of any turn for any player in the following way:
Let's assume you want to have the direction of player 1 between turns 6 and 7. It is now turn 22.
- Just write a function: getDirection(agentID, startingTurn)
- Then, walk through the map with a loop. Search for a square with 'agentID' agentID and 'takenOnTurn' startingTurn.
- Save that position.
- Then, search the four squares next to it (or just all squares again; who cares) for 'agentID' agentID and 'takenOnTurn' (startingTurn + 1).
- Now it's easy to determine the direction.
Don't forget to take a look at the other agents; Lorenz and Saskia!
Please note:
I know the names of the agents given by me as examples may sound somewhat familiar. This is completely coincidental, I swear! (*ahum*)
All the examples are just that: examples. Lorenz = persistent variables, Menno = data parameter and Saskia = basic fitness.
They are not really made to play against each other...
It is up to you and your teammates (if any) to combine the things shown in these examples, and to come up with creative ways to create an agent that will wow.
Best of luck,
~ Scriblink
& TheYsconator
"""
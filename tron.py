# Tested on python version 3.4
##!/usr/local/bin/python3.4

if __name__ == "__main__":
	""" START EDITING HERE """
	import teamred as AI_A
	import lorenz as AI_B
	
	DEV = {
		'debug_competition': True, # Default: False
		'debug_data': True, # Default: False
		#'debug_data_world': True, # Default: False
		'debug_match': True, # Default: False
		'debug_turn': True, # Default: False
		'debug_world': True, # Default: False
		#'display_results': False, # Default: True
		'number_of_matches': 3, # Default: 7
		'world_min_width': 5, # Default: 7
		'world_max_width': 11, # Default: 29
		'world_min_height': 5, # Default: 7
		'world_max_height': 11, # Default: 29
	}
	
	# Please, during your final tests, set this variable to False. It will disable all changes made in the DEV variable
	enableDevMode = True
	
	# You can use the snippet below to make 'finding the top of the run' easier. You may edit this as you like. :-)
	numberOfEmptyLines = 50
	toPrint = ''
	for i in range(0, numberOfEmptyLines):
		toPrint += '\n'
	print(toPrint)
	
	""" STOP EDITING HERE """
	# TRON AI WRAPPER/ 'ENGINE' THINGIE
	# Written by:
	#	 ~ Scriblink
	#	 & TheYsconator
	# VERSION 3.1 (2015)
	
	# The line below will be uncommented during the real competitions. This will disable the DEV variable!
	# enableDevMode = False
	
	import random
	
	class Agent():
		def __init__(self, ai):
			self.reset(ai)
			
		def reset(self, ai):
			self.name = ai.name
			self.turn = ai.turn
			self.alive = True
			self.score = 0
			self.x = None
			self.y = None
			return None
	
	class Competition():
		def __init__(self, agents, dev, numberOfMatches, worldRestrictions):
			self.reset(agents, dev, numberOfMatches, worldRestrictions)
			
		def reset(self, agents, dev, numberOfMatches, worldRestrictions):
			self.agents = agents
			self.dev = dev
			self.numberOfMatches = numberOfMatches
			self.worldRestrictions = worldRestrictions
			self.currentMatch = 0
			return None
			 
		def start(self):
			if self.dev['debug_competition']:
				print('')
				print('Competition info:')
				print('Min world size: %s x %s sq. (W x H)' % (self.worldRestrictions['minWidth'], self.worldRestrictions['minHeight'],))
				print('Max world size: %s x %s sq. (W x H)' % (self.worldRestrictions['maxWidth'], self.worldRestrictions['maxHeight'],))
				print('Number of matches: %s.' % (self.numberOfMatches,))
			for i in range(0, self.numberOfMatches):
				self.currentMatch += 1
				if self.dev['debug_competition']:
					print('')
					print('Starting match %s...' % (self.currentMatch,))
				match = Match(self.agents, self.currentMatch, self.dev, self.numberOfMatches, self.worldRestrictions)
				match.start()
			if self.dev['display_results']:
				print('')
				winner = None
				if self.agents[0].score > self.agents[1].score:
					winner = 0
				elif self.agents[1].score > self.agents[0].score:
					winner = 1
				if winner == None:
					print('The competition ended in a draw with %s points!' % (self.agents[0].score,))
				else:
					loser = 1
					if winner == 1:
						loser = 0
					print('%s won the competition with %s point(s), opposed to %s, which had %s point(s)!' % (self.agents[winner].name, self.agents[winner].score, self.agents[loser].name, self.agents[loser].score))
			return None
	
	class Match():
		def __init__(self, agents, currentMatch, dev, numberOfMatches, worldRestrictions):
			self.reset(agents, currentMatch, dev, numberOfMatches, worldRestrictions)
		
		def reset(self, agents, currentMatch, dev, numberOfMatches, worldRestrictions):
			self.agents = agents
			self.currentMatch = currentMatch
			self.dev = dev
			self.numberOfMatches = numberOfMatches
			self.worldRestrictions = worldRestrictions
			self.currentTurn = 0
			self.world = World(
				width = random.randint(self.worldRestrictions['minWidth'], self.worldRestrictions['maxWidth']),
				height = random.randint(self.worldRestrictions['minHeight'], self.worldRestrictions['maxHeight']),
			)
			coords = self.world.addAgent(
				currentTurn = self.currentTurn,
				agentID = 0,
			)
			self.agents[0].alive = True
			self.agents[0].x = coords['x']
			self.agents[0].y = coords['y']
			coords = self.world.addAgent(
				currentTurn = self.currentTurn,
				agentID = 1,
			)
			self.agents[1].alive = True
			self.agents[1].x = coords['x']
			self.agents[1].y = coords['y']
			if self.dev['debug_match']:
				print('')
				print('Agent \'A\' is %s, with initial position (%s, %s).' % (self.agents[0].name, self.agents[0].x, self.agents[0].y,))
				print('Agent \'B\' is %s, with initial position (%s, %s).' % (self.agents[1].name, self.agents[1].x, self.agents[1].y,))
				print('The world is %s sq wide, and %s sq high.' % (self.world.width, self.world.height))
			if self.dev['debug_world']:
				self.world.debug(
					currentTurn = self.currentTurn,
				)
			return None
			
		def start(self):
			while self.anotherTurnIsNeeded():
				self.currentTurn += 1
				self.turn()
			if self.agents[0].alive:
				self.agents[0].score += 1
			elif self.agents[1].alive:
				self.agents[1].score += 1
			if (self.agents[0].alive) and (self.dev['debug_match']):
				print('')
				print('%s wins this match!' % (self.agents[0].name,))
			elif (self.agents[1].alive) and (self.dev['debug_match']):
				print('')
				print('%s wins this match!' % (self.agents[1].name,))
			elif (self.dev['debug_match']):
				print('')
				print('No agent wins; the match ends in a draw.')
			return None
			
		def anotherTurnIsNeeded(self):
			agentsAlive = 0
			for thisAgent in self.agents:
				if thisAgent.alive:
					agentsAlive += 1
			if agentsAlive >= 2:
				return True
			return False
			
		def continueTurn(self):
			return self.anotherTurnIsNeeded()
			
		def turn(self):
			if self.dev['debug_turn']:
				print('')
				print('Starting turn %s...' % (self.currentTurn,))
			dataToPass = self.gatherDataToSendToAgent()
			if self.dev['debug_data']:
				print('')
				print('Passed data:')
				for key in dataToPass.keys():
					if (key is not 'world_data') or (self.dev['debug_data_world']):
						if key is 'agents':
							print('- %s:' % (key,))
							for i, tmp_agent in enumerate(dataToPass['agents']):
								print('-- %s:' % (i,))
								for tmp_agent_key in tmp_agent.keys():
								  if tmp_agent_key is 'position':
								    print('--- x: %s.' % (tmp_agent['position']['x'],))
								    print('--- y: %s.' % (tmp_agent['position']['y'],))
								  else:
								    print('--- %s: %s.' % (tmp_agent_key, tmp_agent[tmp_agent_key]))
						elif key is 'world_data':
						  print('- world_data:')
						  for y, y_val in enumerate(dataToPass['world_data']):
						    for x, x_val in enumerate(y_val):
						      print('-- (x: %s, y: %s): %s' % (x, y, x_val))
						else:
							print('- %s: %s.' % (key, dataToPass[key],))
			choice_0 = self.agents[0].turn(dataToPass)
			choice_1 = self.agents[1].turn(dataToPass)
			if self.dev['debug_turn']:
				print('')
				print('%s turn return: %s' % (self.agents[0].name, choice_0,))
				print('%s turn return: %s' % (self.agents[1].name, choice_1,))
			choice_0_converted = None
			choice_1_converted = None
			# First, let's check if the choices are valid.
			if self.continueTurn():
				if not self.choiceIsValid(
					choice = choice_0,
				):
					self.agents[0].alive = False
					if self.dev['debug_turn']:
						print('')
						print('%s died, because its choice was not valid.' % (self.agents[0].name,))
				if not self.choiceIsValid(
					choice = choice_1,
				):
					self.agents[1].alive = False
					if self.dev['debug_turn']:
						print('')
						print('%s died, because its choice was not valid.' % (self.agents[1].name,))
			# Then, let's check if the two resulting positions are not the same.
			# If they are, both agents have to die.
			if self.continueTurn():
				choice_0_converted = self.calcChoiceConverted(
					agent = 0,
					choice = choice_0,
				)
				choice_1_converted = self.calcChoiceConverted(
					agent = 1,
					choice = choice_1,
				)
				if (choice_0_converted == choice_1_converted):
					self.agents[0].alive = False
					self.agents[1].alive = False
					if self.dev['debug_turn']:
						print('')
						print('Both agents died, because their resulting positions were the same.')
			# Finally, let's make the moves and update the agent's statusus if needed.
			if self.continueTurn():
				move_result_0 = self.world.moveAgent(
					currentTurn = self.currentTurn,
					agentID = 0,
					newX = choice_0_converted['x'],
					newY = choice_0_converted['y'],
				)
				move_result_1 = self.world.moveAgent(
					currentTurn = self.currentTurn,
					agentID = 1,
					newX = choice_1_converted['x'],
					newY = choice_1_converted['y'],
				)
				if not move_result_0:
					self.agents[0].alive = False
					if self.dev['debug_turn']:
						print('')
						print('%s died, because it\'s bumped into something. Silly agent.' % (self.agents[0].name,))
				if not move_result_1:
					self.agents[1].alive = False
					if self.dev['debug_turn']:
						print('')
						print('%s died, because it\'s bumped into something. Silly agent.' % (self.agents[1].name,))
			# Oh, and we'll have to update the positions of the agents if needed! ^_^
			if self.continueTurn():
				self.agents[0].x = choice_0_converted['x']
				self.agents[0].y = choice_0_converted['y']
				self.agents[1].x = choice_1_converted['x']
				self.agents[1].y = choice_1_converted['y']
			# And debug the world if needed...
			if self.dev['debug_world'] and self.continueTurn():
				self.world.debug(
					currentTurn = self.currentTurn,
				)
			return None
		
		def choiceIsValid(self, choice):
			return choice in ['NORTH', 'EAST', 'SOUTH', 'WEST']
		
		def calcChoiceConverted(self, agent, choice):
			x = self.agents[agent].x
			y = self.agents[agent].y
			if choice == 'NORTH':
				y -= 1
			elif choice == 'EAST':
				x += 1
			elif choice == 'SOUTH':
				y += 1
			elif choice == 'WEST':
				x -= 1
			return {
				'x': x,
				'y': y,
			}
			
		def gatherDataToSendToAgent(self):
			data = {
				'match_current': self.currentMatch,
				'match_total': self.numberOfMatches,
				'agents': [
					{
						'id': 0,
						'name': self.agents[0].name,
						'position': {
							'x': self.agents[0].x,
							'y': self.agents[0].y,
						},
						'score': self.agents[0].score,
					},
					{
						'id': 1,
						'name': self.agents[1].name,
						'position': {
							'x': self.agents[1].x,
							'y': self.agents[1].y,
						},
						'score': self.agents[1].score,
					},
				],
				'turn_current': self.currentTurn,
				'world_data': self.world.world,
				'world_height_current': self.world.height,
				'world_width_current': self.world.width,
				'world_height_limit_lower': self.worldRestrictions['minHeight'],
				'world_height_limit_upper': self.worldRestrictions['maxHeight'],
				'world_width_limit_lower': self.worldRestrictions['minWidth'],
				'world_width_limit_upper': self.worldRestrictions['maxWidth'],
			}
			return data
	
	class World():
		def __init__(self, width, height):
			self.reset(width, height)
		
		def reset(self, width, height):
			self.width = width
			self.height = height
			self.world = []
			for y in range(0, self.height):
				thisLine = []
				for x in range(0, self.width):
					thisLine.append({
						'agentID': None,
						'takenOnTurn': None,
					})
				self.world.append(thisLine)
			return None

		def addAgent(self, currentTurn, agentID):
			x = random.randint(0, self.width - 1)
			y = random.randint(0, self.height - 1)
			while self.world[y][x]['agentID'] != None:
				x = random.randint(0, self.width - 1)
				y = random.randint(0, self.height - 1)
			self.world[y][x]['agentID'] = agentID
			self.world[y][x]['takenOnTurn'] = currentTurn
			return {
				'x': x,
				'y': y,
			}
			
		def removeAgent(self, agentID):
			for y in range(0, self.height):
				for x in range(0, self.width):
					if self.world[y][x]['agentID'] == agentID:
						self.world[y][x] = {
							'agentID': None,
							'takenOnTurn': None,
						}
			return None
		
		def moveAgent(self, currentTurn, agentID, newX, newY):
			if not self.isOnWorld(
				x = newX,
				y = newY,
			):
				return False
			if self.isOccupied(
				x = newX,
				y = newY,
			):
				return False
			self.world[newY][newX]['agentID'] = agentID
			self.world[newY][newX]['takenOnTurn'] = currentTurn
			return True
		
		def debug(self, currentTurn):
			print('')
			if currentTurn == 0:
				print('Starting positions:')
			for y in range(0, len(self.world)):
				line = []
				for x in range(0, len(self.world[y])):
					symbol = self.world[y][x]
					if symbol['agentID'] == None:
						line.append('_')
					elif symbol['takenOnTurn'] == currentTurn:
						if symbol['agentID'] == 0:
							line.append('A')
						else:
							line.append('B')
					elif symbol['takenOnTurn'] < currentTurn:
						if symbol['agentID'] == 0:
							line.append('a')
						else:
							line.append('b')
					else:
						line.append('_')
				print(line)
			return None
			
		def isOnWorld(self, x, y):
			if (x >= 0) and (y >= 0) and (x < self.width) and (y < self.height):
				return True
			return False
	
		def isOccupied(self, x, y):
			if self.world[y][x]['agentID'] != None:
				return True
			return False
	
	pass_dev = {
		'debug_competition': False,
		'debug_data': False,
		'debug_data_world': False,
		'debug_match': False,
		'debug_turn': False,
		'debug_world': False,
		'display_results': True,
	}
	
	pass_number_of_matches = 7
	
	pass_world_restrictions = {
		'minWidth': 7,
		'maxWidth': 29,
		'minHeight': 7,
		'maxHeight': 29,
	}
	
	if enableDevMode:
		print('')
		print('DEV MODE ENABLED')
		if 'debug_competition' in DEV.keys():
			pass_dev['debug_competition'] = DEV['debug_competition']
		if 'debug_data' in DEV.keys():
			pass_dev['debug_data'] = DEV['debug_data']
		if 'debug_data_world' in DEV.keys():
			pass_dev['debug_data_world'] = DEV['debug_data_world']
		if 'debug_match' in DEV.keys():
			pass_dev['debug_match'] = DEV['debug_match']
		if 'debug_turn' in DEV.keys():
			pass_dev['debug_turn'] = DEV['debug_turn']
		if 'debug_world' in DEV.keys():
			pass_dev['debug_world'] = DEV['debug_world']
		if 'display_results' in DEV.keys():
			pass_dev['display_results'] = DEV['display_results']
		if 'number_of_matches' in DEV.keys():
			pass_number_of_matches = DEV['number_of_matches']
		if 'world_min_width' in DEV.keys():
			pass_world_restrictions['minWidth'] = DEV['world_min_width']
		if 'world_max_width' in DEV.keys():
			pass_world_restrictions['maxWidth'] = DEV['world_max_width']
		if 'world_min_height' in DEV.keys():
			pass_world_restrictions['minHeight'] = DEV['world_min_height']
		if 'world_max_height' in DEV.keys():
			pass_world_restrictions['maxHeight'] = DEV['world_max_height']

	competition = Competition(
		agents = [
			Agent(AI_A),
			Agent(AI_B),
		],
		dev = pass_dev,
		numberOfMatches = pass_number_of_matches,
		worldRestrictions = pass_world_restrictions,
	)
	competition.start()
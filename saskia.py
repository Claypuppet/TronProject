"""
ONDERAAN HEB IK WAT LAST MINUTE NOTITIES GESCHREVEN; misschien handig om eerst te lezen ^_^.
"""

# The name of the agent. This is a REQUIRED STRING.
name = 'Saskia'

# The turn function. This FUNCTION is REQUIRED. It has one passed parameter: the 'data' parameter. To see what's in it, just print the contents to the console.
# The turn function has a RETURN of type STRING. There are four options: 'NORTH', 'EAST', 'SOUTH' and 'WEST'.
# Make sure you always return one of these (no typos), as failing to do so will result in a match loss...
# Also note: if a match hangs/ breaks while the wrapper was working on your turn, you will lose that match!

def turn(data):
  # You'll have to fill in resulting_position yourself, if you need it.
	options = [
    {
      'fitness': 0,
      'option': 'NORTH',
      'resulting_position': {
        'x': None,
        'y': None,
      },
    },
    {
      'fitness': 0,
      'option': 'EAST',
      'resulting_position': {
        'x': None,
        'y': None,
      },
    },
    {
      'fitness': 0,
      'option': 'SOUTH',
      'resulting_position': {
        'x': None,
        'y': None,
      },
    },
    {
      'fitness': 0,
      'option': 'WEST',
      'resulting_position': {
        'x': None,
        'y': None,
      },
    },
	]
	
	preferences = [
    {
      'description': 'Agent will not die by hitting a wall.', # The description is just for yourself, to keep stuff neat.
      'function': willNotHitWall,
      'score': 3,
    },
    {
      'description': 'Agent will have some free space.',
      'function': willHaveSomeSpace,
      'score': 10,
    },
	]
	
	# Check all the preferences on all the options.
	for option in options:
	  for preference in preferences:
	    if preference['function'](option):
	      option['fitness'] += preference['score']

	return determineBestOption(options)
	
# Some sample fitness function...
# I know, they aren't really useful...
def willNotHitWall(option):
  if (option['option'] == 'EAST') or (option['option'] == 'SOUTH'):
    return True
  return False
  
def willHaveSomeSpace(option):
  import random
  
  i = random.randint(0, 1)
  if i == 1:
    return True
  return False
	
# Returns the option with the highest fitness value.
# If there are more with the same highest value, it returns one of those at random.
# You should avoid this! (You should avoid using the random function.)
def determineBestOption(options):
  import random
  
  highestFitnessFound = 0
  bestOptions = []
  for option in options:
    if option['fitness'] == highestFitnessFound:
      bestOptions.append(option)
    elif option['fitness'] > highestFitnessFound:
      bestOptions = []
      bestOptions.append(option)
      highestFitnessFound = option['fitness']
  
  if len(bestOptions) == 1:
    return bestOptions[0]['option']
  else:
    bestOptionIndex = random.randint(0, len(bestOptions) - 1)
    return bestOptions[bestOptionIndex]['option']

"""
Some notes on the Saskia agent:
The Saskia agent is based on a fitness function system, which means that its final decision depends purely on factual considerations. This is one of the most basic programming structures when writing an 'intelligent' agent, but there are many more! You can do some research if you want to, but don't spend too much time on that: writing a good fitness function can get your agent very far, very quickly...
Don't forget to take a look at the other agents; Lorenz and Menno!
Please note:
I know the names of the agents given by me as examples may sound somewhat familiar. This is completely coincidental, I swear! (*ahum*)
All the examples are just that: examples. Lorenz = persistent variables, Menno = data parameter and Saskia = basic fitness.
They are not really made to play against each other...
It is up to you and your teammates (if any) to combine the things shown in these examples, and to come up with creative ways to create an agent that will rock.
Best of luck,
~ Scriblink
& TheYsconator
"""

"""
LAST MINUTE NOTITIES:
Oke even in het Nederlands; een snelle laatste notitie over de fitness functie.
De fitness functie is een type functie die veel gebruikt wordt bij het oplossen van problemen door middel van computers. Er zijn soortgelijke functies, zoals de 'functie voor het berekenen van het minste verlies', maar als je niet bekend bent met dit soort functies raad ik je aan de fitness functie methode te gebruiken, als je er al een kiest (je kunt natuurlijk ook gewoon blijven programmeren zoals je altijd doet; dat kan je tijd schelen).
In het kort: De fitnessfunctie bepaalt wat de best mogelijke oplossing voor een probleem is, aan de hand van feiten.
Een voorbeeld:
Voorkeuren van agent: Agent wil een portie fruit mee nemen, om deze later op te eten of eventueel deels of in zijn geheel uit te delen.
Beperkingen van agent: Agent kan 1 portie fruit pakken en meenemen.
Opties: [een appel], [een paar druiven], [een paar kersen] en [een citroen]
Voorkeuren (naam, omschrijving, score (0-10)):
	V_1: Is deels uit te delen, zodat ik ook nog wat over heb voor mijzelf. 7
	V_2: Geeft geen nare vlekken als je knoeit. 9
	V_3: Kan zoet zijn. 2
	V_4: Is nooit zuur. 9
	V_5: Is niet uit te delen, maar ik heb lekker veel voor mijzelf. 8
	
Als we hier de porties fruit doorheen halen krijgen we:
- Appel: V_2 (9) + V_3 (2) + V_5 (8) = 9 + 2 + 8 = 19
- Druiven: V_1 (7) + V_2 (9) + V_3 (2) = 7 + 9 + 2 = 18
- Kersen: V_1 (7) + V_3 (2) + V_4 (9) = 7 + 2 + 9 = 18
- Citroen: V_2 (9) + V_5 (8) = 9 + 8 = 17
De appel komt er dus het beste uit, met 19 punten.
Een paar voordelen van deze methode zijn dat het erg makkelijk is om voorkeuren toe te voegen, en de waarde van voorkeuren aan te passen.
In de Saskia agent heb ik alles een beetje uitgeschreven (langdradig geschreven), dan kun je alles optimaliseren zoals je het zelf wilt...
"""
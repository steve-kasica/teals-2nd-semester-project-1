
# Step 1: Display story title

title = 'Space Opera: a Mad Lib.'
print(title)

welcome = 'Welcome! You are about to play a fantastic word game. I will ask you for nouns, verbs, adjectives, and proper nouns. Using those words I will create an unexpected story for you!'
print(welcome)

# Step 2: Prompt user for words

adj1 = input('Give me an adjective: ')
noun1 = input('Give me a plural noun: ')
adj2 = input('Give me another adjective: ')
noun2 = input('Give me a proper noun: ')
noun3 = input('Give me a different plural noun: ')
verb1 = input('Give me a verb: ')
noun4 = input('Give me another proper noun: ').upper()
noun5 = input('Give me a different noun: ')
verb2 = input('Give me a different verb: ')
noun6 = input('Who is the coolest girl in school? ')

# Step 3: Assemble story

story1 = 'It is a period of ' + adj1 + ' war. Rebel '  + noun1 + ' striking from a hidden base, have won their ' + adj2 + ' victory against the evil ' + noun2 + '. ' 

story2 = 'During the battle, Rebel ' + noun1 + ' managed to ' + verb1 + ' secret ' + noun3 + ' to the ' + noun2 + '\'s ultimate weapon, the ' + noun4 + ', an armored space station with enough ' + noun5 + ' to ' + verb2 + ' an entire planet. '

story3 = 'Pursued by ' + noun2 + '\'s sinister agents, Princess ' + noun6 + ' races home aboard her starship, custodian of the stolen ' + noun3 + ' that can save her people and restore freedom to the galaxy.....'

# Step 4: Display story

print(story1 + story2 + story3)
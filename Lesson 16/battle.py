import time
import random

print()
print('-' * 65)
print()

print('A wild Wartortle appears!')
time.sleep(0.3)
print('...the background music changes...')
time.sleep(0.3)
print('You only have one Pokemon, Leekbird!')
time.sleep(0.3)
print('I choose you Leekbird!!!')
time.sleep(0.3)
print()

# set the starting health values
leekbird_hp = 250
wartortle_hp = 250

print('starting HP:')
time.sleep(0.3)
print('leekbird HP: ' + str (leekbird_hp))
time.sleep(0.3)
print('wartortle HP: ' + str(wartortle_hp))
time.sleep(0.3)
print()

#This is a battle loop
while leekbird_hp > 0 and wartortle_hp > 0:
	print('Choose your battle move:')
	time.sleep(0.3)
	print('- [1] Punch 👊')
	time.sleep(0.3)
	print('- [2] Wet Willy 👂')
	time.sleep(0.3)
	print('- [3] Fire 🔥')
	time.sleep(0.3)
	print('- [4] Rap Battle 🎤')
	time.sleep(0.3)
	print()

	player_move = input('Pick a move using corresponding number: ')
	player_move = int(player_move)

	if player_move == 1:
		wartortle_hp == wartortle_hp - 25
		print('Leekbird uses Punch 👊 and deals 25 HP of damage. ')
	elif player_move == 2:
		damage = random.randint(5,40)
		wartortle_hp = wartortle_hp - damage
		print('Leekbird uses Wet Willy 👂 and deals ' + str(damage) + ' HP of damage. ')
	elif player_move == 3:
		leekbird_hp = leekbird_hp + 100
		print('Leekbird uses Fire 🔥 and recovers 100 HP.')

	time.sleep(0.3)
	print()

	# enemy battle choices
	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		leekbird_hp = leekbird_hp - 30
		print('Wartortle uses a Spitball and deals 30 HP of damage.')
	elif enemy_move == 2:
		leekbird_hp = leekbird_hp - 20 
		wartortle_hp = wartortle_hp + 20
		print('Wartortle uses Drink Blood 💉 and deals 20 HP of damage while also recovering 20 HP of health.')

	time.sleep(0.3)
	print()

	if leekbird_hp < 0:
		leekbird_hp = 0
	if wartortle_hp < 0:
		wartortle_hp = 0

	print('Updated HP: ')
	time.sleep(0.3)
	print('Leekbird HP: ' + str(leekbird_hp))
	time.sleep(0.3)
	print("Wartortle HP: " + str(wartortle_hp))
	time.sleep(0.3)
	print ()

if leekbird_hp > 0 and wartortle_hp == 0:
	print('Wild wartortle has failed. Leekbird wins!')
	time.sleep(0.3)
if leekbird_hp == 0 and wartortle_hp > 0:
	print('Leekbird has fainted. Wild wartortle wins!')
	time.sleep(0.3)
	print('You have no remaining Pokemon, you lose.')
	time.sleep(0.3)



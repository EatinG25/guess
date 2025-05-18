import random
ans = random.randint(1, 100)
t = 0
while True:
	g = input('Please guess a number from 1 to 100:')
	g = int(g)
	t = t + 1
	if g == ans:
		print('Bingo!')
		break
	elif g > ans:
		print('The answer is smaller.')
	elif g < ans:
		print('The answer is bigger.')
print('You guessed', t, 'times.')
import random
start = input('Start from:')
end = input('End to:')
start = int(start)
end = int(end)
ans = random.randint(start, end)
t = 0
while True:
	g = input('Please guess a number:')
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
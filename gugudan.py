def gugudan1():
	for i in range(2,10):
		for j in range(2,10):
			a = i * j
			print(i, 'x', j, '=', str(a).rjust(2), ' ',end='')
			if j == 5:
				print('\n',end='')
		print('\n')

# gugudan1()

def gugudan2():
	for i in range(2,10):
		for j in range(2,10):
			a = i * j
			if j <= 5:
				print(j, 'x', i, '=', str(a).rjust(2), ' ',end='')
				if j == 5:
					print('\n',end='')
	print('\n')	
	for i in range(2,10):
		for j in range(2,10):
			a = i * j
			if 5 < j <= 9:
				print(j, 'x', i, '=', str(a).rjust(2), ' ',end='')
				if j == 9:
					print('\n',end='')
gugudan2()


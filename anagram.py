def all():
	l = []
	for a in range(10):
		for b in range(10):
			for c in range(10):
				for d in range(10):
					num = str(a) + str(b) + str(c) + str(d)
					l.append(num)
	return l

alist2 = []

def anagram(list):
	for i in list:
		alist = []
		for j in range(4):
			alist.append(i[j])
		alist.sort()
		alist2.append(alist)
		alist = []

	alist3 = []

	for i in range(len(alist2)-1):
		if not i in alist3:
			alist4 = [list[i]]
			j = i+1
			while j < len(alist2):
				if alist2[i] == alist2[j]:
			   		alist4 = alist4 + [list[j]]
			   		alist3 = alist3 + [j]
				j = j + 1
				
			if alist4 != [list[i]]:
				for k in alist4:
					if alist4.index(k) == len(alist4) - 1:
						print(k)						
					else :
						print(k,end=' ')
l = all()
anagram(l)

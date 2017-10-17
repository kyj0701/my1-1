def anagram(list):
	ilist = []
	slist = []
	for i in list:
		for j in range(4):
			ilist.append(i[j])
		ilist.sort()
		slist.append(ilist)
		ilist = []

	
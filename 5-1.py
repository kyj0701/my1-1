x=4
ss=[1,3,6,7]
s=[4,7,2,5,9,1]
left=[1,4,5,8]
right=[2,3,6,9]

def insert0(x,ss):
	if ss != []:
		if x <= ss[0]:
			return [x] + ss
		else:
			return [ss[0]] + insert0(x,ss[1:])
	else:
		return [x]

def insert1(x,ss):
	def loop(ss,left):
		if ss != []:
			if x <= ss[0]:
				return left + [x] + ss
			else:
				return loop(ss[1:],left+[ss[0]])
		else:
			return left + [x] + ss
	return loop (ss,[])

def insert2(x,ss):
	left = []
	while ss != []:
		if x <= ss[0]:
			return left + [x] + ss
		else:
			ss, left = ss[1:], left +[ss[0]]
	return left + [x] + ss

def isort1(s):
	def loop(s,ss):
		if s != []:
			return loop(s[1:],insert(s[0],))

print ("insert0(x,ss)",insert0(x,ss))
print ("insert1(x,ss)",insert1(x,ss))
print ("insert2(x,ss)",insert2(x,ss))
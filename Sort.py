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
	return loop(ss,[])


def insert2(x,ss):
	left =[]
	while ss != []:
		if x <= ss[0]:
			return left + [x] + ss
		else:
			ss, left = ss[1:], left + [ss[0]]
	return left + [x] + ss


def isort1(s):
	def loop(s,ss):
		if s != []:
			return loop(s[1:],insert2(s[0],ss))
		else:
			return ss
	return loop(s,[])


def isort2(s):
	ss = []
	while s != []:
		s, ss = s[1:], insert2(s[0],ss)
	return ss


def isort3(s):
	ss = []
	for _ in s:
		s, ss = s[1:], insert2(s[0],ss)
	return ss


def merge1(left,right):
	def loop(left,right,ss):
		if not (left == [] or right == []):
			if left[0] <= right[0]:
				ss.append(left[0])
				return loop(left[1:],right,ss)
			else:
				ss.append(right[0])
				return loop(left,right[1:],ss)
		else:
			return ss
	return loop(left,right,[])


def merge2(left,right):
	ss = []
	while not (left == [] or right == []):
		if left[0] <= right[0]:
			ss.append(left[0])
			left = left[1:]
		else:
			ss.append(right[0])
			right = right[1:]
	return ss


def bsort(s):
	for k in range(0,len(s)-1):
		for i in range(0,len(s)-1):
			if s[i] > s[i+1]:
				s[i], s[i+1] = s[i+1], s[i]
	return s


print ("insert0(x,ss)",insert0(x,ss))
print ("insert1(x,ss)",insert1(x,ss))
print ("insert2(x,ss)",insert2(x,ss))
print ("isort1(s)",isort1(s))
print ("isort2(s)",isort2(s))
print ("isort3(s)",isort3(s))
print ("merge1(left,right)",merge1(left,right))
print ("merge2(left,right)",merge2(left,right))
print ("bsort(s)",bsort(s))
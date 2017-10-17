import random
list2 = []
list3 = []
alist1 = []
alist2 = []


def create_init_board(size):
	list1 = []
	list2 = []
	for i in range(size**2):
		list1.append(i)
	random.shuffle(list1)
	for i in range(size):
		alist1 = []
		alist1 = list1[size * i : size*(i+1)]
		list2.append(alist1)
	return list2
	# return [[0,15,14,13], [12,11,10,9], [8,7,6,5], [4,3,2,1]]


def set_goal_board(size):
	list1 = []
	list3 = []
	for i in range(1,size**2):
		list1.append(i)
	for i in range(size):
		if i == size-1:
			list1.append(0)
		alist2 = []
		alist2 = list1[size * i : size*(i+1)]
		list3.append(alist2)
	return list3


def print_board(board):  # board
	for i in board:
		for j in i:
			if j == 0:
				print("  ",end=' ')
			else:
				print(str(j).rjust(2),end=' ')
		print("\n")

def get_number(size):
	num = input("Type the number you want to move (Type 0 to quit): ")
	while not (num.isdigit() and 0 <= int(num) <= size**2-1) :
		num = input("Type the number you want to move (Type 0 to quit): ")
	return int(num)

def find_position(num,board):  # nun, board
	for i in range(int(size)):
		for j in range(int(size)):
			if num == board[i][j]:
				return (i,j)

def move(pos, empty, board):  # pos, empty, board
	(x,y) = pos
	if empty == (x-1,y) or empty == (x+1,y) or empty == (x,y-1) or empty == (x,y+1):
		board[empty[0]][empty[1]] = board[x][y]
		board[x][y] = 0
		return (pos,board)
	else:
		print("Can't move! Try again.")
		return (empty,board)

def sliding_puzzle(size):
	board = create_init_board(size)
	goal = set_goal_board(size)
	empty = find_position(0, board)
	while True:
		print_board(board)
		if board == goal:
			print("Congratulations!")
			break
		num = get_number(size)
		if num == 0:
			break
		pos = find_position(num, board)
		(empty, board) = move(pos, empty, board)
	print("Please come again.")
	
if __name__ == "__main__": 
	import sys 
	size = sys.argv[1] 
	if size.isdigit() and int(size) > 1: 
		sliding_puzzle(int(size))
	else: 
		print("Not a proper system argument.")


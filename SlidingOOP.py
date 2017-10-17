import random
list2 = []
list3 = []
alist1 = []
alist2 = []

class Reader:
	@staticmethod
	def get_number(size):
		num = input("Type the number you want to move (Type 0 to quit): ")
		while not (num.isdigit() and 0 <= int(num) <= size**2-1) :
			num = input("Type the number you want to move (Type 0 to quit): ")
		return int(num)

class SlidingBoard:
	@staticmethod
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
			board = list2
		return board

	@staticmethod
	def create_goal_board(size):
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
			gboard = list3
		return gboard

	@property
	def board(self):
		return self.__board

	def find_position(self,num):  # num, board
		for i in range(len(self.__board)):
			for j in range(len(self.__board)):
				if num == self.__board[i][j]:
					return (i,j)

	def print_board(self):  # board
		for i in self.__board:
			for j in i:
				if j == 0:
					print("  ",end=' ')
				else:
					print(str(j).rjust(2),end=' ')
			print("\n")

	def move(self, pos):  # pos, empty, board
		(x,y) = pos
		if self.__empty == (x-1,y) or self.__empty == (x+1,y) or self.__empty == (x,y-1) or self.__empty == (x,y+1):
			self.__board[self.__empty[0]][self.__empty[1]] = self.__board[x][y]
			self.__board[x][y] = 0
			# return (pos,self.__board)
			self.__empty = pos
		else:
			print("Can't move! Try again.")
			# return (self.__empty,self.__board)

	def __init__(self,size):
		self.__board = SlidingBoard.create_init_board(size)
		self.__empty = self.find_position(0)

class SlidingPuzzleController:
	def __init__(self,size):
		self.__size = size
		self.__slider = SlidingBoard(size)
		self.__goal = self.__slider.create_goal_board(size)

	def play(self):
		size = self.__size
		goal = self.__goal
		empty = self.__slider.find_position(0)
		while True:
			self.__slider.print_board()
			if self.__slider.board == goal:
				print("Congratulations!")
				break
			num = Reader.get_number(size)
			if num == 0:
				break
			pos = self.__slider.find_position(num)
			self.__slider.move(pos)
		print("Please come again.")

def main():
	import sys
	size = sys.argv[1]
	if size.isdigit() and int(size) > 1:
		SlidingPuzzleController(int(size)).play()
	else:
		print("Not a proper system argument.")

main()


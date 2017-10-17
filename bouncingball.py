from tkinter import *

class Box:
	def __init__(self, size, bsize, color):
		self.size = size
		self.color = color
		self.bsize = bsize
		
	def in_horizontal_contact(self, x):
		return x <= 0 or x >= self.size
		
	def in_vertical_contact(self, y):
		return y <= 0 or y >= self.size

	def in_ball_contact(self, x1, y1, x2, y2, bsize):
		x = x1
		y = y1
		d2 = self.bsize
		return (x - d2 <= x2 and x2 <= x + d2) and (y - d2 <= y2 and y2 <= y + d2)
		
class MovingBall:
	def __init__(self, x1, y1, x2, y2, xv, yv, x2v, y2v, color, color2, size, size2, shake, box):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.xv = xv
		self.x2v = x2v
		self.yv = yv
		self.y2v = y2v
		self.color = color
		self.color2 = color2
		self.size = size
		self.size2 = size2
		self.shake = shake
		self.box = box
	# 	self.otherBalls = []

	# def addBall(self, ball):
	# 	self.otherBalls.append(ball)

	# def deleteBall(self):
	# 	self.otherBalls = []

	def move(self, time_unit):
		i = self.box.size
		j = self.shake.size
		self.x1 = self.x1 + self.xv * time_unit
		if self.box.in_horizontal_contact(self.x1):
			self.xv = - self.xv
		self.y1 = self.y1 + self.yv * time_unit
		if self.box.in_vertical_contact(self.y1):
			self.yv = - self.yv

		self.x2 = self.x2 + self.x2v * time_unit
		if self.box.in_horizontal_contact(self.x2):
			self.x2v = - self.x2v
		self.y2 = self.y2 + self.y2v * time_unit
		if self.box.in_vertical_contact(self.y2):
			self.y2v = - self.y2v

		if (i-j)/2 <= self.x1 <= (i+j)/2 and (i-j)/2 <= self.y1 <= (i+j)/2:
			self.xv = -self.xv
			self.yv = -self.yv
		if (i-j)/2 <= self.x2 <= (i+j)/2 and (i-j)/2 <= self.y2 <= (i+j)/2:
			self.x2v = -self.x2v
			self.y2v = -self.y2v

		if self.box.in_ball_contact(self.x1, self.y1, self.x2, self.y2, j/2):
			self.xv = -self.xv
			self.yv = -self.yv
			self.x2v = -self.x2v
			self.y2v = -self.y2v


class AnimationWriter:
	def __init__(self, root, ball, shake, box):
		self.size = box.size
		size = self.size
		self.canvas = Canvas(root, width=size, height=size)
		self.canvas.grid()
		self.ball = ball
		self.shake = shake

	def animate(self):
		self.canvas.delete(ALL)
		self.ball.move(1)
		x1 = self.ball.x1
		x2 = self.ball.x2
		y1 = self.ball.y1
		y2 = self.ball.y2
		d = self.ball.size * 2
		d2 = self.ball.size2 * 2
		d3 = self.shake.size
		c = self.ball.color
		c2 = self.ball.color2
		c3 = self.shake.color
		a = (self.size - d2)/2
		b = (self.size - d2)/2
		self.canvas.create_oval(x1, y1, x1+d , y1+d, outline=c, fill=c)
		self.canvas.create_oval(x2, y2, x2+d2 , y2+d2, outline=c2, fill=c2)
		self.canvas.create_rectangle(a, b, a+d3, b+d3, outline=c3, fill=c3)
		self.canvas.after(10, self.animate)
		
class BounceController:
	def __init__(self):
		box_size = 400
		box_color = 'white'
		ball_size = 10
		ball_size2 = 10
		shake_size = 40
		ball_color = 'red'
		ball2_color = 'green'
		shake_color = 'blue'
		x_velocity, y_velocity = 5, 2
		root = Tk()
		root.title("Bouncing Ball")
		root.geometry(str(box_size+10)+"x"+str(box_size+10))
		box = Box(box_size, ball_size * 2, box_color)
		shake = Box(shake_size, ball_size * 2, shake_color)
		ball = MovingBall(box_size//5, box_size//3, box_size//2, box_size//4, x_velocity, y_velocity, x_velocity, y_velocity, ball_color, ball2_color, ball_size, ball_size2, shake, box)
		AnimationWriter(root, ball, shake, box).animate()
		root.mainloop()
	
BounceController()
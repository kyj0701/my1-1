from tkinter import *

class App(Frame):
	def __init__(self, window):
		super().__init__(window)
		self.pack(padx=20, pady=20)
		Label(self, text="Hello, world!", bg="yellow", fg="red").grid(row=0,column=0)
		Button(self, text="Quit", command=self.quit).grid(row=1,column=0)
		self.c = Canvas(window, width=20, height=20)
		self.c.grid(row=1,column=1)

window = Tk()
window.title("Hello")
window.geometry("400x400")
App(window)
window.mainloop()



		# self.pack(padx=20, pady=20, fill=X)
		# h = Label(self, text="Hello, world!")
		# h['bg'] = "yellow"
		# h['fg'] = "red"
		# h.pack(fill=X)
		#
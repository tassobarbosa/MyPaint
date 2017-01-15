from Tkinter import *

#--Global variables, used to allow tools on the drawboard
flagline = 0

class TopBar:
	def __init__(self, root):
		self.root = root
		self.menu = Menu(root)
		self.menuFile = Menu(self.menu)
		self.menuEdit = Menu(self.menu)
		self.menuView = Menu(self.menu)
		self.menuImage = Menu(self.menu)
		self.menuOptions = Menu(self.menu)
		self.menuHelp = Menu(self.menu)
		self.menu.add_cascade(label = "File", menu = self.menuFile)
		self.menu.add_cascade(label = "Edit", menu = self.menuEdit)
		self.menu.add_cascade(label = "View", menu = self.menuView)
		self.menu.add_cascade(label = "Image", menu = self.menuImage)
		self.menu.add_cascade(label = "Options", menu = self.menuOptions)
		self.menu.add_cascade(label = "Help", menu = self.menuHelp)

  		self.menuFile.add_command(label="New")
		self.menuFile.add_command(label="Open")
		self.menuFile.add_command(label="Save")
		self.menuFile.add_command(label="Exit", command = self.exit)
		self.root.configure(menu = self.menu)

	def exit(self):
		self.root.destroy()

class Tools:
	def __init__(self,root):
		self.root = root
		self.frame = Frame(root)
		self.frame.grid(column=1,row=1,sticky=N+W)				
		self.buttons = []
		self.last_btn_id = 0

		#Buttons definitios


		#id = 0
		self.img_pencil = PhotoImage(file='icons/pencil.png')
		self.pencil = Button(self.frame, command = self.btn_Pencil, image = self.img_pencil)	
		self.pencil.grid(column=1,row=1,sticky=N+E+S+W)	
		self.buttons.append(self.pencil)


		#id = 1
		self.img_line = PhotoImage(file='icons/pencil-1.png')	
		self.line = Button(self.frame, command = self.btn_Line, image = self.img_line)	
		self.line.grid(column=2,row=1,sticky=N+E+S+W)	
		self.buttons.append(self.line)

	def btn_Pencil(self):
		global flagline

		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.pencil['relief'] = RIDGE			
		self.last_btn_id = 0
			
		flagline = 0	

	def btn_Line(self):
		global flagline

		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.line['relief'] = RIDGE	
		self.last_btn_id = 1
	
		flagline = 1	

class DrawBoard:	
	def __init__(self, root):
		self.canvas = Canvas(root, width=600, height=300, bg='white')
		self.canvas.grid(column=2,row=1)
	
		self.canvas.bind('<1>',self.drawLine)

	def drawLine(self,event):
		if flagline == 1:
			x_origin = self.canvas.winfo_rootx()
			y_origin = self.canvas.winfo_rooty()
			x_abs = self.canvas.winfo_pointerx()
			y_abs = self.canvas.winfo_pointery()
			try:
				P = (x_abs - x_origin, y_abs - y_origin)
				self.canvas.create_line(self.ultimo_P, P)
				self.ultimo_P = P
			except:
				self.ultimo_P=(x_abs - x_origin, y_abs - y_origin)	

root = Tk()
root.title('MyPaint')
root.geometry("600x300")
bar = TopBar(root)
tools = Tools(root)
draw = DrawBoard(root)
root.mainloop()

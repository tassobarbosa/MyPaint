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
		self.img_line = PhotoImage(file='icons/curve.png')	
		self.line = Button(self.frame, command = self.btn_Line, image = self.img_line)	
		self.line.grid(column=2,row=1,sticky=N+E+S+W)	
		self.buttons.append(self.line)

		#id = 2
		self.img_circle = PhotoImage(file='icons/circle-ruler.png')	
		self.circle = Button(self.frame, command = self.btn_Circle, image = self.img_circle)	
		self.circle.grid(column=1,row=2,sticky=N+E+S+W)	
		self.buttons.append(self.circle)

	def btn_Pencil(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.pencil['relief'] = RIDGE			
		self.last_btn_id = 0
			
		draw.canvas.bind("<Button-1>", draw.novalinha)
		draw.canvas.bind("<B1-Motion>", draw.estendelinha)
		draw.canvas.bind("<ButtonRelease-1>", draw.fechalinha)	

	def btn_Line(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.line['relief'] = RIDGE	
		self.last_btn_id = 1

		draw.canvas.bind('<1>',draw.drawLine)	
		draw.canvas.bind("<B1-Motion>", draw.stretchLine)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeLine)	
	

	def btn_Circle(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.circle['relief'] = RIDGE	
		self.last_btn_id = 2

		draw.canvas.bind('<1>',draw.drawCircle)
		
	

class DrawBoard:	
	def __init__(self, root):
		self.canvas = Canvas(root, width=600, height=300, bg='white')
		self.canvas.grid(column=2,row=1)
		self.x1, self.y1 = 0, 0	
		#self.canvas.bind('<1>',self.drawLine)

	#--DRAW STRAIGHT LINE --
	def drawLine(self,e):		
		self.x1,self.y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.create_line(self.x1, self.y1, self.x1, self.y1, tags="wire_test")

	def stretchLine(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		coords = self.canvas.coords("wire_test") + [x,y]
		self.canvas.coords("wire_test", *coords)

	def closeLine(self,e): 	
		x2, y2 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.delete('wire_test')
		self.canvas.create_line(self.x1,self.y1,x2,y2, tags="wire")
	#-- End of straigth --

	#-- DRAW FREE LINE --
	def novalinha(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		self.canvas.create_line(x,y,x,y, tags="corrente")

	def estendelinha(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		coords = self.canvas.coords("corrente") + [x,y]
		self.canvas.coords("corrente", *coords)

	def fechalinha(self,e): 
		self.canvas.itemconfig("corrente", tags=())	
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
	#-- End of free --


	def selecionalinha(e):
		global x0, y0
		x0, y0 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.itemconfig(CURRENT, tags = "sel")

	def movelinha(e):
		global x0, y0
		x1, y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.move("sel", x1-x0,y1-y0)
		x0, y0=x1,y1

	def deselecionalinha(e):
		self.canvas.itemconfig("sel", tags=())

	def drawCircle(self,event):	
			x_origin = self.canvas.winfo_rootx()
			y_origin = self.canvas.winfo_rooty()
			x_abs = self.canvas.winfo_pointerx()
			y_abs = self.canvas.winfo_pointery()
			
			try:
				P = (x_abs - x_origin, y_abs - y_origin)
				print P
				self.canvas.create_oval(self.ultimo_P, P, tags="corrente")
				self.ultimo_P = P
			except:
				self.ultimo_P=(x_abs - x_origin, y_abs - y_origin)	
"""
c.bind("<Button-3>", selecionalinha)
c.bind("<B3-Motion>", movelinha)
c.bind("<ButtonRelease-3>", deselecionalinha)
"""
root = Tk()
root.title('MyPaint')
root.geometry("600x300")
bar = TopBar(root)
tools = Tools(root)
draw = DrawBoard(root)
root.mainloop()

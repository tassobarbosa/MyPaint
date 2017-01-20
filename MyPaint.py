from Tkinter import *
import webbrowser

class About:
	def __init__(self, master):			
		self.master = master
		self.master.geometry("300x250+200+100")
		self.master.minsize(300,250)  
		self.master.resizable(width=False, height=False)
		self.master.title('Developer')
		Label(self.master,text='Hello!',font=('Verdana','13','bold')).grid()
		self.msg1 = Label(self.master,text="I am glad you are here!").grid()
		self.msg2 = Label(self.master,text="This program was developed by:").grid()

		self.separator = Frame(self.master,height=200, bd=1, relief=RIDGE)
		self.separator.grid(padx=30,pady=15)

		self.name = Label(self.separator,text="\nTasso Barbosa")
		self.name.grid()
		
		self.git = Label(self.separator,text="https://github.com/tassoeb",cursor="hand1")
		self.git.bind("<1>",self.link1)
		self.git.grid()

		self.tube = Label(self.separator,text="https://www.youtube.com/eloybarbosa",cursor="hand1")
		self.tube.bind("<1>",self.link2)
		self.tube.grid()
		
		Label(self.separator,text="\n\n\n").grid()

	def link1(self,event):
		webbrowser.open_new(r"https://www.github.com/tassoeb")
	def link2(self,event):
		webbrowser.open_new(r"https://www.youtube.com/eloybarbosa")


class TopBar:
	def __init__(self, root):
		self.root = root
		self.menu = Menu(root)
		self.menuFile = Menu(self.menu)
		self.menuEdit = Menu(self.menu)
		self.menuView = Menu(self.menu)
		self.menuImage = Menu(self.menu)
		self.menuOptions = Menu(self.menu)
		self.menuAbout = Menu(self.menu)
		self.menu.add_cascade(label = "File", menu = self.menuFile)
		self.menu.add_cascade(label = "Edit", menu = self.menuEdit)
		self.menu.add_cascade(label = "View", menu = self.menuView)
		self.menu.add_cascade(label = "Image", menu = self.menuImage)
		self.menu.add_cascade(label = "Options", menu = self.menuOptions)
		self.menu.add_cascade(label = "Help", menu = self.menuAbout)

  		self.menuFile.add_command(label="New", command = self.new)
		self.menuFile.add_command(label="Open")
		self.menuFile.add_command(label="Save", command = self.save)
		self.menuFile.add_command(label="Exit", command = self.exit)
		self.menuAbout.add_command(label="Developer", command = self.about1)
		self.root.configure(menu = self.menu)


	def exit(self):
		self.root.destroy()

	def new(self):			
		draw.canvas.delete("all")

	def save(self):
		draw.canvas.postscript(file="teste.png", colormode='color')

	def about1(self):
		janela = Tk()
		About(janela)
			
			
class Tools:
	def __init__(self,root):
		self.root = root
		self.frame = Frame(root)
		self.frame.grid(column=1,row=1,sticky=N+W)				
		self.buttons = []
		self.last_btn_id = 0
		self.frame['cursor']='hand1'
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
		
		#id = 3
		self.img_square = PhotoImage(file='icons/select-box.png')	
		self.square = Button(self.frame, command = self.btn_Square, image = self.img_square)	
		self.square.grid(column=2,row=2,sticky=N+E+S+W)	
		self.buttons.append(self.square)

		#id = 4
		self.img_eraser = PhotoImage(file='icons/eraser.png')
		self.eraser = Button(self.frame, command = self.btn_Eraser, image = self.img_eraser)	
		self.eraser.grid(column=1,row=3,sticky=N+E+S+W)	
		self.buttons.append(self.eraser)

		#id = 5
		self.img_brush = PhotoImage(file='icons/paint-brush-2.png')	
		self.brush = Button(self.frame, command = self.btn_Brush, image = self.img_brush)	
		self.brush.grid(column=2,row=3,sticky=N+E+S+W)	
		self.buttons.append(self.brush)

		#id = 6
		self.img_ink = PhotoImage(file='icons/ink.png')	
		self.ink = Button(self.frame, command = self.btn_Ink, image = self.img_ink)	
		self.ink.grid(column=1,row=4,sticky=N+E+S+W)	
		self.buttons.append(self.ink)
		
		#id = 7
		self.img_move = PhotoImage(file='icons/scissors.png')	
		self.move = Button(self.frame, command = self.btn_Move, image = self.img_move)	
		self.move.grid(column=2,row=4,sticky=N+E+S+W)	
		self.buttons.append(self.move)

	def btn_Pencil(self):
		
		draw.thick_line = 1 
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.pencil['relief'] = RIDGE			
		self.last_btn_id = 0

		draw.canvas['cursor'] = 'pencil'	

		draw.canvas.bind("<Button-1>", draw.newLine)
		draw.canvas.bind("<B1-Motion>", draw.stretchLine)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeLine)	

	def btn_Line(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.line['relief'] = RIDGE	
		self.last_btn_id = 1

		draw.canvas['cursor'] = 'pencil'	
		draw.canvas.bind('<1>',draw.drawLine)	
		draw.canvas.bind("<B1-Motion>", draw.stretchLine2)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeLine2)	
	

	def btn_Circle(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.circle['relief'] = RIDGE	
		self.last_btn_id = 2

		draw.canvas['cursor'] = 'crosshair'	
		draw.canvas.bind('<1>',draw.drawCircle)	
		draw.canvas.bind("<B1-Motion>", draw.stretchCircle)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeCircle)	
	

	def btn_Square(self):
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.square['relief'] = RIDGE	
		self.last_btn_id = 3

		draw.canvas['cursor'] = 'crosshair'	
		draw.canvas.bind('<1>',draw.drawSquare)	
		draw.canvas.bind("<B1-Motion>", draw.stretchSquare)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeSquare)	

	def btn_Eraser(self):	
		draw.thick_line = 10 
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.eraser['relief'] = RIDGE	
		self.last_btn_id = 4

		draw.canvas['cursor'] = 'dotbox'	
		color.btn_White()
		draw.canvas.bind("<Button-1>", draw.newLine)
		draw.canvas.bind("<B1-Motion>", draw.stretchLine)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeLine)	
	def btn_Brush(self):			
		draw.thick_line = 6 
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.brush['relief'] = RIDGE	
		self.last_btn_id = 5

		draw.canvas['cursor'] = 'spraycan'	
		
		draw.canvas.bind("<Button-1>", draw.newLine)
		draw.canvas.bind("<B1-Motion>", draw.stretchLine)
		draw.canvas.bind("<ButtonRelease-1>", draw.closeLine)	

	def btn_Ink(self):		
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.ink['relief'] = RIDGE	
		self.last_btn_id = 6

		draw.canvas['cursor'] = 'spraycan'	
		draw.canvas.bind("<Button-1>", draw.InkPaint)
		draw.canvas.unbind("<B1-Motion>")
		draw.canvas.unbind("<ButtonRelease-1>")	

	def btn_Move(self):		
		self.buttons[self.last_btn_id]['relief'] = RAISED
		self.move['relief'] = RIDGE	
		self.last_btn_id = 7

		draw.canvas['cursor'] = 'hand1'	

		draw.canvas.bind("<Button-1>", draw.selectObj)
		draw.canvas.bind("<B1-Motion>", draw.moveObj)
		draw.canvas.bind("<ButtonRelease-1>", draw.leaveObj)	

class DrawBoard:	
	def __init__(self, root):
		self.canvas = Canvas(root, width=740, height=500, bg='white')	
		self.canvas.grid(column=2,row=1)
		self.x1, self.y1 = 0, 0	
		self.thick_line = 0

	#--DRAW STRAIGHT LINE --
	def drawLine(self,e):		
		self.x1,self.y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		l = self.canvas.create_line(self.x1, self.y1, self.x1, self.y1, tags="wire_test")
		self.canvas.itemconfig(l,fill = color.color_vet[color.color_idx])

	def stretchLine2(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		coords = self.canvas.coords("wire_test") + [x,y]
		self.canvas.coords("wire_test", *coords)

	def closeLine2(self,e): 	
		x2, y2 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.delete('wire_test')
		l = self.canvas.create_line(self.x1,self.y1,x2,y2, tags="wire")
		self.canvas.itemconfig(l,fill = color.color_vet[color.color_idx])
	#-- End of straigth --

	#-- DRAW FREE LINE --		
	def newLine(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		l = self.canvas.create_line(x,y,x,y, tags="wire1",width=self.thick_line)	
		self.canvas.itemconfig(l,fill = color.color_vet[color.color_idx])

	def stretchLine(self,e):
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		coords = self.canvas.coords("wire1") + [x,y]				
		self.canvas.coords("wire1", *coords)	

	def closeLine(self,e): 
		self.canvas.itemconfig("wire1", tags=())	
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
	#-- End of free --



	#--DRAW CIRLCE --
	def drawCircle(self,e):		
		self.x1,self.y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		l = self.canvas.create_oval(self.x1, self.y1, self.x1, self.y1, tags="wire_test")
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])
	def stretchCircle(self,e):
		self.canvas.delete('wire_test')
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		l = self.canvas.create_oval(self.x1, self.y1, x, y, tags="wire_test")	
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])

	def closeCircle(self,e): 	
		x2, y2 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.delete('wire_test')
		l = self.canvas.create_oval(self.x1,self.y1,x2,y2, tags="wire")
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])
	#-- End of circle --

	#--DRAW SQUARE --
	def drawSquare(self,e):		
		self.x1,self.y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		l = self.canvas.create_rectangle(self.x1, self.y1, self.x1, self.y1, tags="wire_test")
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])

	def stretchSquare(self,e):
		self.canvas.delete('wire_test')
		x,y = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		l = self.canvas.create_rectangle(self.x1, self.y1, x, y, tags="wire_test")		
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])

	def closeSquare(self,e): 	
		x2, y2 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.canvas.delete('wire_test')
		l = self.canvas.create_rectangle(self.x1,self.y1,x2,y2, tags="wire")
		self.canvas.itemconfig(l,outline = color.color_vet[color.color_idx])
	#-- End of square --

	#-- INK --
	def InkPaint(self,e):		
		self.xx,self.yy = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)
		self.obj = self.canvas.find_closest(self.xx, self.yy)[0]
		self.canvas.itemconfig(self.obj,fill = color.color_vet[color.color_idx])
		
		
	#End of INK

	#--MOVE OBJECT --
	
	def selectObj(self,e):		
		global x0, y0
		x0, y0 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		self.canvas.itemconfig(CURRENT,tags="sel")
		draw.canvas['cursor'] = 'fleur'	
	def moveObj(self,e):
		global x0, y0	
		x1,y1 = self.canvas.canvasx(e.x), self.canvas.canvasy(e.y)	
		self.canvas.move("sel", x1-x0, y1-y0)
		x0, y0 = x1, y1	

	def leaveObj(self,e): 				
		self.canvas.itemconfig("sel",tags=())
		draw.canvas['cursor'] = 'hand1'	
	#-- End of movement --
class Colors:
	def __init__(self,root):
		self.root = root
		self.frame = Frame(root)
		self.frame.grid(column = 1, columnspan=2,row=2,sticky=N+E+S+W)								

		self.frame['cursor']='hand1'
		self.color_vet = []
		self.color_idx = 0

		#Colors definitios
	
		self.pick = Button(self.frame,bg='black',activebackground='white',relief=RIDGE)	
		self.pick.grid(column=1,row=1,rowspan=2,sticky=N+E+S+W)	
	
		#id = 0
		self.black = Button(self.frame, bg='black',activebackground='black',relief=RIDGE, command = self.btn_Black)	
		self.black.grid(column=2,row=1,sticky=N+E+S+W)	
		self.color_vet.append("black")

		#id = 1
		self.white = Button(self.frame, bg='white',activebackground='white',relief=RIDGE, command = self.btn_White)	
		self.white.grid(column=2,row=2,sticky=N+E+S+W)	
		self.color_vet.append("white")

		#id = 2
		self.grey = Button(self.frame, bg='grey',activebackground='grey',relief=RIDGE, command = self.btn_Grey)	
		self.grey.grid(column=3,row=1,sticky=N+E+S+W)	
		self.color_vet.append("grey")

		#id = 3
		self.grey2 = Button(self.frame, bg='ivory3',activebackground='ivory3',relief=RIDGE, command = self.btn_Grey2)	
		self.grey2.grid(column=3,row=2,sticky=N+E+S+W)	
		self.color_vet.append("ivory3")

		#id = 4 
		self.red2 = Button(self.frame, bg='red4',activebackground='red4',relief=RIDGE, command = self.btn_Red2)	
		self.red2.grid(column=4,row=1,sticky=N+E+S+W)	
		self.color_vet.append("red4")

		#id = 5
		self.red = Button(self.frame, bg='red',activebackground='red',relief=RIDGE, command = self.btn_Red)	
		self.red.grid(column=4,row=2,sticky=N+E+S+W)	
		self.color_vet.append("red")
		
		#id = 6 
		self.yellow2 = Button(self.frame, bg='gold3',activebackground='gold3',relief=RIDGE, command = self.btn_Yellow2)	
		self.yellow2.grid(column=5,row=1,sticky=N+E+S+W)	
		self.color_vet.append("gold3")

		#id = 7
		self.yellow = Button(self.frame, bg='yellow',activebackground='yellow',relief=RIDGE, command = self.btn_Yellow)	
		self.yellow.grid(column=5,row=2,sticky=N+E+S+W)	
		self.color_vet.append("yellow")
		
		#id = 8 
		self.green2 = Button(self.frame, bg='springgreen3',activebackground='springgreen3',relief=RIDGE, command = self.btn_Green2)	
		self.green2.grid(column=6,row=1,sticky=N+E+S+W)	
		self.color_vet.append("springgreen3")

		#id = 9
		self.green = Button(self.frame, bg='green',activebackground='green',relief=RIDGE, command = self.btn_Green)	
		self.green.grid(column=6,row=2,sticky=N+E+S+W)	
		self.color_vet.append("green")

		#id = 10 
		self.blue = Button(self.frame, bg='cadetblue1',activebackground='cadetblue1',relief=RIDGE, command = self.btn_Blue)	
		self.blue.grid(column=7,row=1,sticky=N+E+S+W)	
		self.color_vet.append("cadetblue1")

		#id = 11
		self.blue2 = Button(self.frame, bg='cyan4',activebackground='cyan4',relief=RIDGE, command = self.btn_Blue2)	
		self.blue2.grid(column=7,row=2,sticky=N+E+S+W)	
		self.color_vet.append("cyan4")

		#id = 12 
		self.blue3 = Button(self.frame, bg='blue',activebackground='blue',relief=RIDGE, command = self.btn_Blue3)	
		self.blue3.grid(column=8,row=1,sticky=N+E+S+W)	
		self.color_vet.append("blue")

		#id = 13
		self.blue4 = Button(self.frame, bg='darkblue',activebackground='darkblue',relief=RIDGE, command = self.btn_Blue4)	
		self.blue4.grid(column=8,row=2,sticky=N+E+S+W)	
		self.color_vet.append("darkblue")

		#id = 14 
		self.pink = Button(self.frame, bg='hotpink',activebackground='hotpink',relief=RIDGE, command = self.btn_Pink)	
		self.pink.grid(column=9,row=1,sticky=N+E+S+W)	
		self.color_vet.append("hotpink")

		#id = 15
		self.purple = Button(self.frame, bg='purple',activebackground='purple',relief=RIDGE, command = self.btn_Purple)	
		self.purple.grid(column=9,row=2,sticky=N+E+S+W)	
		self.color_vet.append("purple")

		#id = 16 
		self.orange = Button(self.frame, bg='darkorange',activebackground='darkorange',relief=RIDGE, command = self.btn_Orange)	
		self.orange.grid(column=10,row=1,sticky=N+E+S+W)	
		self.color_vet.append("darkorange")

		#id = 17
		self.brown = Button(self.frame, bg='sienna4',activebackground='sienna4',relief=RIDGE, command = self.btn_Brown)	
		self.brown.grid(column=10,row=2,sticky=N+E+S+W)	
		self.color_vet.append("sienna4")


	def btn_Black(self):
		self.pick['bg'] = 'black'
		self.color_idx = 0

	def btn_White(self):
		self.pick['bg'] = 'white'
		self.color_idx = 1

	def btn_Grey(self):
		self.pick['bg'] = 'grey'
		self.color_idx = 2

	def btn_Grey2(self):
		self.pick['bg'] = 'ivory3'
		self.color_idx = 3

	def btn_Red2(self):
		self.pick['bg'] = 'red4'
		self.color_idx = 4

	def btn_Red(self):
		self.pick['bg'] = 'red'
		self.color_idx = 5

	def btn_Yellow2(self):
		self.pick['bg'] = 'gold3'
		self.color_idx = 6

	def btn_Yellow(self):
		self.pick['bg'] = 'yellow'
		self.color_idx = 7

	def btn_Green2(self):
		self.pick['bg'] = 'springgreen3'
		self.color_idx = 8

	def btn_Green(self):
		self.pick['bg'] = 'green'
		self.color_idx = 9

	def btn_Blue(self):
		self.pick['bg'] = 'cadetblue1'
		self.color_idx = 10

	def btn_Blue2(self):
		self.pick['bg'] = 'cyan4'
		self.color_idx = 11

	def btn_Blue3(self):
		self.pick['bg'] = 'blue'
		self.color_idx = 12

	def btn_Blue4(self):
		self.pick['bg'] = 'darkblue'
		self.color_idx = 13

	def btn_Pink(self):
		self.pick['bg'] = 'hotpink'
		self.color_idx = 14

	def btn_Purple(self):
		self.pick['bg'] = 'purple'
		self.color_idx = 15

	def btn_Orange(self):
		self.pick['bg'] = 'darkorange'
		self.color_idx = 16

	def btn_Brown(self):
		self.pick['bg'] = 'sienna4'
		self.color_idx = 17
root = Tk()
root.title('MyPaint')
root.minsize(810,570)
bar = TopBar(root)
tools = Tools(root)
draw = DrawBoard(root)
color = Colors(root)
root.mainloop()

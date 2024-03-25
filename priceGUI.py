from tkinter import *
from PIL import Image, ImageTk
import subprocess
import time 
import autoTrade
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
windowSize = str(height)+'x'+str(width)
bgColour = '#1E5E59'
options= ['Scar-20', 'Negev', 'Scout']
selectedOption = StringVar(root)
selectedOption.set('Make a Select')
graphHeight = height*0.25

def get_prices():
	low = autoTrade.get_lowest_price()
	vol = autoTrade.get_volume()
	med = autoTrade.get_median_price()
	print(low)
	print(med)
	print(vol)

def get_width(wdgt):
	widthW = wdgt.winfo_width()
	print(widthW)

def point_flip(pointY, height):
	y = height - pointY
	return y

def on_resize(event):
	width = event.width
	height = event.height

def draw_line(canvas,oldX,oldY,newX,newY):
	canvas.create_line(oldX,oldY,newX,newY,fill='green',width=2)

#This will be changed to draw the price graph later
def draw_square(pointY,pointX):
	
	oldY = pointY
	oldX = pointX
	newX = oldX + 25
	newY = oldY
	#Line1
	draw_line(graphFrame,oldX,oldY,newX,newY)
	oldX=newX
	oldY=newY
	newX=oldX
	newY=oldY-25
	#Line2
	draw_line(graphFrame,oldX,oldY,newX,newY)
	oldX=newX
	oldY=newY
	newX=oldX-25
	newY=oldY 
	#Line3		
	draw_line(graphFrame,oldX,oldY,newX,newY)
	oldX=newX
	oldY=newY
	newX=oldX
	newY=oldY+25
	#Line4
	draw_line(graphFrame,oldX,oldY,newX,newY)
	#draw_line(graphFrame,0,0,25,pointY)
					

root.geometry(windowSize)
root.bind('<Configure>', on_resize)
root.configure(bg=bgColour)
root.minsize(int(width*0.75),int(height*0.75))


#image = Image.open('Scar20.jpeg')
#photo = ImageTk.PhotoImage(image)
#displayImage = Label(root,image=photo,bd=0,highlightthickness=0, width=265,height=200,bg='#206963')
outputs = Canvas(root,bd=0,highlightthickness=0,bg='#283030',height=str(height*0.25),width=width*0.10)
itemMenu = OptionMenu(root,selectedOption,*options)
graphFrame = Canvas(root,bd=0,highlightthickness=0,bg='#283030',height=str(height*0.25),width=width)
button = Button(root, text = "testButton",command = get_prices)


#displayImage.pack(anchor='nw',pady=10,padx=5)
itemMenu.pack(anchor='w',padx=10)
graphFrame.pack(side=BOTTOM,pady=10,padx=10)
button.pack(anchor='e',padx=10)
outputs.place(relx=0.005,rely=0.5,anchor='w', x=-0, y=-50,relwidth=0.1,relheight=0.4)


draw_square(point_flip(100,graphHeight),graphWidth)


root.mainloop()

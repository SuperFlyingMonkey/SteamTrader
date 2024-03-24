from tkinter import *
from PIL import Image, ImageTk
import time 
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
windowSize = str(height)+'x'+str(width)
bgColour = '#1E5E59'
options= ['Scar-20', 'Negev', 'Scout']
selectedOption = StringVar(root)
selectedOption.set('Make a Select')
graphHeight = height*0.25

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
root.minsize(650,400)


image = Image.open('Scar20.jpeg')
photo = ImageTk.PhotoImage(image)
displayImage = Label(root,image=photo,bd=0,highlightthickness=0, width=265,height=200,bg='#206963')
itemMenu = OptionMenu(root,selectedOption,*options)
graphFrame = Canvas(root,bd=0,highlightthickness=0,bg='#283030',height=str(height*0.25),width=width)


displayImage.pack(anchor='nw',pady=10,padx=5)
itemMenu.pack(anchor='w',padx=10)
graphFrame.pack(side=BOTTOM,pady=10,padx=5)


draw_square(point_flip(100,graphHeight),150)	

root.mainloop()

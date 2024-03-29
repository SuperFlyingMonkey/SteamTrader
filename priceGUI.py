from tkinter import *
from PIL import Image, ImageTk
import subprocess
import time 
import autoTrade

def get_prices(name):
	print(name)
	low = autoTrade.get_lowest_price(name)
	vol = autoTrade.get_volume(name)
	med = autoTrade.get_median_price(name)
	print(low)
	print(med)
	print(vol)

#gets width of any widget 
def get_width(wdgt):
	widthW = wdgt.winfo_width()
	print(widthW)

#make it so that the origin point of the graph in in the bottom left and not the default top left 
def point_flip(pointY, height):
	y = height - pointY
	return y


def on_resize(event):
	width = event.width
	height = event.height
	graphFrame.delete('line')
	graphHeight = graphFrame.winfo_height()
	draw_square(point_flip(3,graphHeight),3)


def draw_line(canvas,oldX,oldY,newX,newY,colour):
	canvas.create_line(oldX,oldY,newX,newY,fill=colour,width=2, tags='line')

#get values from autoTrade.py

	


#This will be changed to draw the price graph later
def draw_square(pointY,pointX):
	
	colour = 'green'
	oldY = pointY
	oldX = pointX
	newX = oldX + 25
	newY = oldY
	#Line1
	draw_line(graphFrame,oldX,oldY,newX,newY,colour)
	oldX=newX
	oldY=newY
	newX=oldX
	newY=oldY-25
	#Line2
	draw_line(graphFrame,oldX,oldY,newX,newY,colour)
	oldX=newX
	oldY=newY
	newX=oldX-25
	newY=oldY 
	#Line3		
	draw_line(graphFrame,oldX,oldY,newX,newY,colour)
	oldX=newX
	oldY=newY
	newX=oldX
	newY=oldY+25
	#Line4
	draw_line(graphFrame,oldX,oldY,newX,newY,colour)

def set_Image(*options):
	imageName = selectedOption.get()
	img = Image.open(imageName)
	photo = ImageTk.PhotoImage(img)
	displayImage.config(image=photo)
	displayImage.image = photo

	get_prices(imageName)



root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
imageFile = 'noPhoto.jpeg'
windowSize = str(height)+'x'+str(width)
bgColour = '#1E5E59'
options= ['noPhoto.jpeg','Scar20.jpeg', 'negev.jpeg', 'scout.jpeg']
selectedOption = StringVar(root)
selectedOption.set('noPhoto.jpeg')



					

#***build GUI***
root.geometry(windowSize)
root.bind('<Configure>', on_resize)
root.title("SkinsPrices")
root.configure(bg=bgColour)
root.minsize(int(width*0.75),int(height*0.90))



outputs = Canvas(root,bd=0,highlightthickness=0.5,bg='#283030',height=str(height*0.25),width=259*1.15)
displayImage = Label(outputs,bd=0,highlightthickness=0, width=265,height=200,bg='#206963')
itemMenu = OptionMenu(outputs, selectedOption, *options, command=set_Image)
graphFrame = Canvas(root,bd=0,highlightthickness=0.5,bg='#283030',height=str(height*0.25),width=width)
graphWidth= graphFrame.winfo_width()

displayImage.pack(anchor='nw',pady=20,padx=5)
itemMenu.pack(anchor='w',padx=10)
graphFrame.place(relx=0.005,rely=1.0, anchor='sw', x=-0,y=-10,relheight=0.25, relwidth=0.99)
outputs.place(relx=0.005,rely=0.05,anchor='nw', x=-0, y=-50,relheight=0.75)
#*****************
set_Image()



root.mainloop()

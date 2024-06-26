from tkinter import *
from PIL import Image, ImageTk
import subprocess
import time 
import autoTrade


#gets width of any widget 
def get_width(wdgt):
	widthW = wdgt.winfo_width()
	print(widthW)

#make it so that the origin point of the graph is on the bottom left and not the default top left 
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

	#get and display data (done in set_Image so data changes to match image)
	low = autoTrade.get_lowest_price(imageName)
	vol = autoTrade.get_volume(imageName)
	med = autoTrade.get_median_price(imageName)
	lowest.config(text='lowest:'+ low, fg='#ffffff')
	median.config(text='median:'+ med,fg='#ffffff')
	volume.config(text='volume:'+ vol,fg='#ffffff')


root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
imageFile = 'noPhoto.jpeg'
windowSize = str(int(width*0.75))+'x'+str(int(height*0.85))
bgColour = '#1E5E59'
options= ['noPhoto.jpeg','Scar20.jpeg', 'negev.jpeg', 'scout.jpeg']
selectedOption = StringVar(root)
selectedOption.set('noPhoto.jpeg')


#***build GUI***
root.geometry(windowSize)
root.bind('<Configure>', on_resize)
root.title("SkinsPrices")
root.configure(bg=bgColour)
root.minsize(int(width*0.50),int(height*0.60))


outputs = Canvas(root,bd=0,highlightthickness=0.5,bg='#283030',height=int(height*0.25),width=259*1.15)
displayImage = Label(outputs,bd=0,highlightthickness=0, width=265,height=200,bg='#206963')
valueBox = Label(outputs,bd=0,highlightthickness=0,bg='#206963',height= 50,width= int(outputs.winfo_width()*30))
itemMenu = OptionMenu(outputs, selectedOption, *options, command=set_Image)
lowest = Label(valueBox,bd=0, highlightthickness=0, width=25,text='lowest', height =2, bg=bgColour)
median = Label(valueBox,bd=0, highlightthickness=0, width=25,text='median', height =2, bg=bgColour)
volume = Label(valueBox,bd=0, highlightthickness=0, width=25,text='volume', height =2, bg=bgColour)


graphFrame = Canvas(root,bd=0,highlightthickness=0.5,bg='#283030',height=int(height*0.25),width=width)
graphWidth= graphFrame.winfo_width()


displayImage.pack(anchor='nw',pady=20,padx=5)
itemMenu.pack(anchor='w',padx=10)
valueBox.pack(anchor='sw',padx=10,pady=5)
lowest.place(anchor='nw', rely=0.12,relwidth=0.65, relheight=0.1)
median.place(anchor='nw', rely=0.24,relwidth=0.65, relheight=0.1)
volume.place(anchor='nw', rely=0.36,relwidth=0.65, relheight=0.1)
graphFrame.place(relx=0.005,rely=1.0, anchor='sw', x=-0,y=-10,relheight=0.25, relwidth=0.99)
outputs.place(relx=0.005,rely=0.05,anchor='nw', x=-0, y=-50,relheight=0.75)
#*****************
set_Image()



root.mainloop()

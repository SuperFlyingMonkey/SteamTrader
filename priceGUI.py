from tkinter import *
from PIL import Image, ImageTk 
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
windowSize = str(height)+'x'+str(width)
bgColour = '#1E5E59'
options= ['Scar-20', 'Negev', 'Scout']
selectedOption = StringVar(root)
selectedOption.set('Make a Select')
oldY = 0
oldX = 0
newX = 10
newY = 5


def on_resize(event):
	width = event.width
	height = event.height

def draw_line(canvas,oldX,oldY,newX,newY):
	canvas.create_line(oldX,oldY,newX,newY,fill='green',width=2)


		
root.geometry(windowSize)
root.bind('<Configure>', on_resize)
root.configure(bg=bgColour)
root.minsize(650,400)



image = Image.open('Scar20.jpeg')
photo = ImageTk.PhotoImage(image)



displayImage = Label(root,image=photo,bd=0,highlightthickness=0, width=265,height=200,bg='#206963')

displayImage.pack(anchor='nw',pady=10,padx=5)

itemMenu = OptionMenu(root,selectedOption,*options)
itemMenu.pack(anchor='w',padx=10)

graphFrame = Canvas(root,bd=0,highlightthickness=0,bg='#283030',height=str(height*0.25),width=width)

graphFrame.pack(side=BOTTOM,pady=10,padx=5)

draw_line(graphFrame,oldX,oldY,newX,newY)
	

root.mainloop()

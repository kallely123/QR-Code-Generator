from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
def generate_qr():
    link_name=entry1.get()
    link=entry2.get()
    file=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file,scale=7)
    image=ImageTk.PhotoImage(Image.open(file))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)
canvas=Canvas(root,height=1000,width=1000)
canvas.pack()
label0=Label(root,text="QR CODE - GENERATOR",fg="dark green",font=('Arial',50))
label4=Label(root,text="STEPS TO GENERATE YOUR QR_CODE \n setp1:Enter your website name in the above LINK NAME \n step2:Copy the http:// url ithe above box named LINK NAME.\n sep3:Clik on GENERATE")
canvas.create_window(200,240,window=label4)
label1=Label(root,text="Link name:",fg='grey')
label2=Label(root,text="Link:",fg='grey')
canvas.create_window(200,50,window=label0)
canvas.create_window(200,100,window=label1)
canvas.create_window(200,160,window=label2)
entry1=Entry(root,bg="pink")
entry2=Entry(root,bg="pink")
canvas.create_window(200,130,window=entry1)
canvas.create_window(200,180,window=entry2)
button=Button(root,text="Generate",bg='sky blue',command=generate_qr)
canvas.create_window(300,180,window=button)

root.mainloop()

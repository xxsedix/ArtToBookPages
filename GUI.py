# Import Module
import tkinter as tk
import random
import os
import PIL
import glob
from PIL import Image, ImageFont, ImageDraw
import time
import automa
 
# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("ArtAutomation Apk")

# Set geometry(widthxheight)
root.geometry('450x200')

#define varaiables
sourcepath_var=tk.StringVar()
savepath_var=tk.StringVar()
alphapath_var=tk.StringVar()
side_var=tk.StringVar()
cordimg_var=tk.StringVar()
txtsize_var=tk.StringVar()
rgbval_var=tk.StringVar()
txtcord_var=tk.StringVar()
 
# lables for tk
lb1 = tk.Label(root, text = "Source Path: ", anchor='w')
lb2 = tk.Label(root, text = "Save Path: ", anchor='w')
lb3 = tk.Label(root, text = "Alpha Path: ", anchor='w')
lb4 = tk.Label(root, text = "Side (R/L): ", anchor='w')
lb5 = tk.Label(root, text = "Cordinates (156, 256, 156): ", anchor='w')
lb6 = tk.Label(root, text = "Text Size (60): ", anchor='w')
lb7 = tk.Label(root, text = "Text RGB color (18, 16, 35): ", anchor='w')
lb8 = tk.Label(root, text = "Cordinates of txt (156, 2190, 3520): ", anchor='w')
f1 = tk.Frame(root)

#add txt to var
lb1.grid(sticky = 'w', column=0,row=0)
lb2.grid(sticky = 'w',column =0, row =1)
lb3.grid(sticky = 'w',column =0, row =2)
lb4.grid(sticky = 'w',column =0, row =3)
lb5.grid(sticky = 'w',column =0, row =4)
lb6.grid(sticky = 'w',column =0, row =5)
lb7.grid(sticky = 'w',column =0, row =6)
lb8.grid(sticky = 'w',column =0, row =7)
f1.grid(row=8, column=1, sticky="e")

 
# adding tk.Entry Field
sourcepath_lb = tk.Entry(root, width=40, textvariable = sourcepath_var)
sourcepath_lb.insert(0, "Location of images")
savepath_lb = tk.Entry(root, width=40, textvariable = savepath_var)
savepath_lb.insert(0, "Location where you want them to save")
alphapath_lb = tk.Entry(root, width=40, textvariable = alphapath_var)
alphapath_lb.insert(0, "Location of alpha file")
side_lb = tk.Entry(root, width=40, textvariable = side_var)
cordimg_lb = tk.Entry(root, width=40, textvariable = cordimg_var)
cordimg_lb.insert(0, "156,256,156")
txtsize_lb = tk.Entry(root, width=40, textvariable = txtsize_var)
txtsize_lb.insert(0, "60")
rgbval_lb = tk.Entry(root, width=40, textvariable = rgbval_var)
rgbval_lb.insert(0, "18,16,35")
txtcord_lb = tk.Entry(root, width=40, textvariable = txtcord_var)
txtcord_lb.insert(0, "156,2190,3520")


# function to display user text when
# tk.Button is clicked
def start():
    sourcepath = sourcepath_var.get()
    savepath = savepath_var.get()
    alphapath = alphapath_var.get()
    side = side_var.get()
    cordimg = cordimg_var.get()
    txtsize = txtsize_var.get()
    rgbval = rgbval_var.get()
    txtcord = txtcord_var.get()
    automa.proxi(sourcepath, savepath, alphapath, side, cordimg, txtsize, rgbval, txtcord);


 
def preview():
	sourcepath = sourcepath_var.get()
	alphapath = alphapath_var.get()
	side = side_var.get()
	cordimg = cordimg_var.get()
	txtsize = txtsize_var.get()
	rgbval = rgbval_var.get()
	txtcord = txtcord_var.get()
	automa.preview(sourcepath, alphapath, side, cordimg, txtsize, rgbval, txtcord);



# tk.Button widget with red color text inside
btn = tk.Button(f1, text = "Start" ,
             fg = "black", command=start)

btn1 = tk.Button(f1, text = "Preview" ,
             fg = "black", command=preview)


sourcepath_lb.grid(column =1, row =0)
savepath_lb.grid(column =1, row =1)
alphapath_lb.grid(column =1, row =2)
side_lb.grid(column =1, row =3)
cordimg_lb.grid(column =1, row =4)
txtsize_lb.grid(column =1, row =5)
rgbval_lb.grid(column =1, row =6)
txtcord_lb.grid(column =1, row =7)
btn.pack(side="left")
btn1.pack(side="right")

 
# Execute Tkinter
root.mainloop()
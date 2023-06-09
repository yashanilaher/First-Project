from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()  # root is size of screen
root.geometry("800x800")


def play_gif():  # will run gif with the help of tkinter
    root.lift()  # it will bring it at top of widgets and remains at top of other windows
    root.attributes("-topmost", True)
    global img
    img = Image.open("giphy.gif") # it opens gif using puthon imaging library 
    lb = Label(root)  # it will create a widget which will display gif animation
    lb.place(x=0, y=0)  # label is place at (x=0 and y=0)

    # will run the loop which will blit image on screen so that gif will be visible
    mixer.music.load("bomb.mp3")  # playing music
    mixer.music.play()

    for img in ImageSequence.Iterator(img): # image sequence module is used form pil to iterate each frame  of gif
        img = img.resize((1000, 800))  # so image is according to size
        img = ImageTk.PhotoImage(img) # it converts the resize frame into tkinter compatible image
        lb.config(image=img)  # will update the label widget's to current frame 
        root.update()  # every time while running it will refresh to show updated window
        time.sleep(0.05)  # 0.05 sec delay is made between each frame so that speed of animation is controlled
    root.destroy()  # will destroy the window and end the programme


play_gif()
root.mainloop()

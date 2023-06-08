from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()  # root is size of screen
root.geometry("800x800")


def play_gif():  # will run gif with the help of tkinter
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("giphy.gif")
    lb = Label(root)
    lb.place(x=0, y=0)  # label is place at (x=0 and y=0)

    # will run the loop which will blit image on screen so that gif will be visible
    i = 0
    mixer.music.load("bomb.mp3")  # playing music
    mixer.music.play()

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 800))  # so image is according to size
        img = ImageTk.PhotoImage(img)
        lb.config(image=img)
        root.update()  # every time while running
        time.sleep(0.05)  # so that it will run for few time ie 0.05 sec
    root.destroy()


play_gif()
root.mainloop()

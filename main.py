from tkinter import *
from ciao3d import *
import time

win=Tk()

win.title("3D Renderer")
win.geometry("1920x1080")

canvas=Canvas(win, width = 1920, height = 1080)
canvas.pack()

#canvas.create_line(100,200,200,35, fill="black", width=5)
list = []
spawnCube(list,1000,0,0,100)


world= World(list, canvas)
for i in range(0, 2000):
    canvas.delete("all")
    world.render(i)
    win.update()
    time.sleep(0.001)
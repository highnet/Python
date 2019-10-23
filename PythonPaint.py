from tkinter import *
import tkinter.font
import subprocess
import os
import io
from io import BytesIO
from PIL import Image

class PaintApp:
    drawing_tool = "pencil"
    left_but = "up"
    x_pos, y_pos = None, None
    canvasWidth = 200
    canvasHeight = 200

    def left_but_down(self,event):
        self.left_but = "down"

    def left_but_up(self,event):
        self.left_but = "up"
        self.x_pos = None
        self. y_pos = None

    def motion(self,event):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)
            print(event.x)
            print(event.y)

    def pencil_draw(self,event):
        if self.left_but == "down":
                if (self.x_pos is not None and self.y_pos is not None):
                    event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth=TRUE,fill = 'black', width=1, tag="line")

                self.x_pos = event.x
                self.y_pos = event.y

    def screenshot(event,drawing_area):
        ps = drawing_area.postscript(colormode='color')
        out = BytesIO()
        Image.open(BytesIO(ps.encode('utf-8'))).save(out, format="PNG")
        out.seek(0)
        return send_file(out, mimetype='image/png')

    def __init__(self,root):
        drawing_area = Canvas(root,width=self.canvasWidth,height=self.canvasHeight)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

        b1 = Button(root, text="Clear", command=lambda: drawing_area.delete("all"))
        b1.pack()
        b1.bind("<Button-1>")

        b2 = Button(root, text="Screenshot",command=lambda:self.screenshot(drawing_area))
        b2.pack()
        b2.bind("<Button-1>")

root = Tk()
paint_app = PaintApp(root)
root.geometry('+%d+%d'%(0,0))
root.mainloop()

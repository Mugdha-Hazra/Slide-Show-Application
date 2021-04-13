from itertools import cycle
import tkinter as tk
import os
from tkinter.filedialog import askdirectory

image_files = []

scriptDir = os.getcwd()  # directory from where script was ran

os.chdir(scriptDir)

for file in os.listdir(scriptDir):
    if file.endswith('.GIF'):  # change this for extension
        realdir = os.path.realpath(file)
        image_files .append(file)


class App(tk.Tk):
    # Tk window/label adjusts to size of image
    def __init__(self, image_files, x, y, delay):

        tk.Tk.__init__(self)

        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        # cycle through the images and display them

        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)

        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set milliseconds time between slides
delay = 500
# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are

# Image.size gives a 2-tuple and the width, height can be obtained

x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()

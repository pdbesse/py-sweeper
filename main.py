from tkinter import *
import defs
import utils

root = Tk()
# override the settings of the window
root.configure(bg='black')
root.geometry(f'{defs.WIDTH}x{defs.HEIGHT}')
root.title('Py-Sweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # change later to black
    width=defs.WIDTH, 
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='blue', # change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='green', # change later to black
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

#run the rundow
root.mainloop()
from tkinter import *


root = Tk()
# override the settings of the window
root.configure(bg='black')
root.geometry('1440x720')
root.title('Py-Sweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # change later to black
    width=1440, 
    height=180
)
top_frame.place(x=0,y=0)

#run the rundow
root.mainloop()
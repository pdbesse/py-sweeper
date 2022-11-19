from tkinter import *
from cell import Cell
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
    bg='black',  # change later to black
    width=defs.WIDTH,
    height=utils.height_prct(25)
)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Py-Sweeper',
    font=('', 48,)
)

game_title.place(
    x = utils.width_prct(25),
    y = 0
)

top_frame.place(
    x=0,
    y=0
)

left_frame = Frame(
    root,
    bg='black',  # change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(
    x=0,
    y=utils.height_prct(25)
)

center_frame = Frame(
    root,
    bg='black',  # change later to black
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(defs.GRID_SIZE):
    for y in range(defs.GRID_SIZE):
        c = Cell(x,  y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()


# run the rundow
root.mainloop()

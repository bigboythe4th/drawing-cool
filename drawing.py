import tkinter as tk 



#custom funtions
def draw():
    x1 = int(txtX1.get())
    y1 = int(txtY1.get())
    x2 = int(txtX2.get())
    y2 = int(txtY2.get())
    Canvas.create_line(x1,y1,x2,y2)


def clear():
    Canvas.delete('all')



#window propeties   
window = tk.Tk()
window.title("Grahping with Tkinter")
window.geometry("800x800")




#creat labels 
lblX1 = tk.Label(window, text="X1: ")
lblY1 = tk.Label(window, text="Y1: ")
lblX2 = tk.Label(window, text="X2: ")
lblY2 = tk.Label(window, text="Y2: ")




#create textboxes
txtX1 = tk.Entry(window)
txtY1 = tk.Entry(window)
txtX2 = tk.Entry(window)
txtY2 = tk.Entry(window)


#buttons
btn = tk.Button(window, text="draw!", padx=20, command=draw)
btnClear = tk.Button(window,text="clear", padx=20,command=clear)


#canvases
Canvas = tk.Canvas(window)


#add GUI item to the grid
lblX1.grid(row=0, column =0)
lblY1.grid(row=1, column =0)
lblX2.grid(row=2, column =0)
lblY2.grid(row=3, column =0)
txtX1.grid(row=0, column =1)
txtY1.grid(row=1, column =1)
txtX2.grid(row=2, column =1)
txtY2.grid(row=3, column =1)
btn.grid(row=3, column = 3)
btnClear.grid(row=3, column = 4)
Canvas.grid(row=4, column=0)


#build window 
window.mainloop()



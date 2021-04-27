from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')


f = ("Times bold", 14)
 
def nextPage():
    ws.destroy()
    import choice

def prevPage():
    ws.destroy()
    import uploadtry

Label(
    ws,
    text="Smile! the camera is going to turn on",
    padx=20,
    pady=20,

    font=('Helvetica',20, 'bold')
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Next Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()


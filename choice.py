from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#639AC4'

f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import page3

def prevPage():
    ws.destroy()
    import page4
    
Label(
    ws,
    text="Choose the action you wish to carry out",
    padx=20,
    pady=20,
    
    font=('Helvetica',20, 'bold')
).pack(expand=True, fill=BOTH)



Button(
    ws, 
    text="Withdraw", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Deposit", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()

from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#639AC4'

f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import page2

    
Label(
    ws,
    text="V-PAY",
    padx=20,
    pady=20,
    bg='#639AC4',
    font=('Helvetica',100, 'bold')
).pack(expand=True, fill=BOTH)

Label(
    text="We have developed a system to make your payment easier and secure.\n You can achive this in 2 simple steps.\nStep 1:Provide your finger print.\nStep 2:Smile when the camera turns on.",
    fg="white",
    bg="black",
    width=10,
    height=10
)




Button(
    ws, 
    text="Next Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()

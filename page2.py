from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')


f = ("Times bold", 14)
 
def nextPage():
    ws.destroy()
    #import page3
    import uploadtry

def prevPage():
    ws.destroy()
    import page1

Label(
    ws,
    text="We have developed a system to make your payment easier and secure.\n\n\n You can achive this in 2 simple steps.Step 1:Provide your finger print.\nStep 2:Smile when the camera turns on.",
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
    text="NextPage", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()



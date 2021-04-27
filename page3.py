import tkinter as tk
import csv
import pandas as pd
import datetime
from datetime import date
from datetime import datetime

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Enter Amount')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type in amount:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():
    name='Nishita Dash'
    x1 = entry1.get()
    x1=int(x1)
    print(x1)
    dat = pd.read_excel ('C://Users//Dell//anaconda3//envs//myenv//biometrics-project//Book1.xlsx',engine='openpyxl')
    df = pd.DataFrame(dat, columns = ['name','amount'])
    df=df.dropna()
    indexes = df[df['name'] == name].index
    if len(indexes)==0:
        print("Name not in database, please check with the department")
    else:
        print("Hello "+name)
        df_pd=(df.at[indexes[0],'amount'])
        print("Your Balance Money is", df_pd)
        b=int(df_pd+x1)
        df.amount[indexes[0]]=b
        print("New bal",b)
        label3 = tk.Label(root, text= 'The Balance is' + str(b),font=('helvetica', 10))
        canvas1.create_window(200, 210, window=label3)
    
button1 = tk.Button(text='Submit', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

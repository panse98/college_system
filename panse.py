from tkinter import filedialog
from tkinter import *
import openpyxl

import  tkinter as Tk
import pandas as pd
root = Tk.Tk()
data = pd.read_excel (r'course_details.xlsx')
df = pd.DataFrame(data,columns= ['course','details'])
df = pd.DataFrame(data)
print (df) # for debugging

T = Tk.Text(root, height=20, width=30)
T.place(x=65, y=10)
height = 1
width = 1
#for i in range(height): #Rows
 #   for j in range(width): #Columns
T.insert(12.0, data)



root.mainloop()

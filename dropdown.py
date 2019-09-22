import xlrd
import subprocess
from tkinter import *
import tkinter as ttk
wb=xlrd.open_workbook(r"D:\data\typedata.xlsx")
sheet = wb.sheet_by_index(0)
l=[]
lpath=[]
for i in range(sheet.nrows):
    l.append(sheet.cell_value(i, 1))
    lpath.append(sheet.cell_value(i, 2))

s=dict(zip(l[1:], lpath[1:]))
m = ttk.Tk()
m.title("Tk dropdown")
m.geometry("300x250")
m.configure(bg="grey")
v=StringVar(m)
v.set("Type")
w=ttk.OptionMenu(m,v,*l)
Label(m,text="Select Application name :",bg="grey").grid(row = 1, column =1)
w.grid(row=1,column=5)
def change_dropdown(*args): 
    if(v.get()!="Type"):
       subprocess.Popen(s.get(v.get()))      


v.trace('w', change_dropdown)
m.mainloop()

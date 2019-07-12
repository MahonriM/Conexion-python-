import sqlite3
from tkinter import *
def conexion():
    conn=sqlite3.connect("")
    lbl.configure(text="Estas conectado")
vtn=Tk()
vtn.iconbitmap("logo.ico")
vtn.title("Conexion con Sqlite")
lbl=Label(vtn,text="")
lbl.grid(column=1,row=1,sticky=(W,E))
btn=Button(vtn,text="Conectar",command=conexion)
btn.grid(column=1,row=2)
vtn.mainloop()
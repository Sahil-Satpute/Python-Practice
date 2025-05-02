
import qrcode
import tkinter as tk
from tkinter import messagebox
def genrator():
    data = entry.get()
    if data:
        ar =qrcode.make(data)
        ar.save("qrcode.png")
        messagebox.showinfo("success","qrcode.png is generated as")
    else:
        messagebox.showwarning("Not successfull","Re enter the link or sentance ")
sahil = tk.Tk()
sahil.title("Qr code genrater")
sahil.geometry("500x300")

label = tk.Label(sahil,text="Enter the link \ sentance for crating qr code")
label.pack()
entry = tk.Entry(sahil,width=20)
entry.pack()
button = tk.Button(sahil,text="Genrate qr code",command=genrator)
button.pack()
sahil.mainloop()

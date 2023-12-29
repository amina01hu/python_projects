from tkinter import *

window=Tk()

btn0=Button(window, text="7", fg="blue", height="2", width="2")
btn1=Button(window, text="8", fg="blue", height="2", width="2")
btn2=Button(window, text="9", fg="blue", height="2", width="2")
btn3=Button(window, text="10", fg="blue", height="2", width="2")
btn0.place(x=0, y=100)
btn1.place(x=50, y=100)
btn2.place(x=100, y=100)
btn3.place(x=0, y=150)
window.title("Pin Pad Machine")
window.geometry("230x295+250+250")
window.mainloop()

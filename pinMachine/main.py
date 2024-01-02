from tkinter import *

window=Tk()

btn0=Button(window, text="7", fg="blue", height="3", width="3")
btn1=Button(window, text="8", fg="blue", height="3", width="3")
btn2=Button(window, text="9", fg="blue", height="3", width="3")
btn3=Button(window, text="10", fg="blue", height="3", width="3")
btn4=Button(window, text="9", fg="blue", height="3", width="3")
btn5=Button(window, text="10", fg="blue", height="3", width="3")
btn0.place(x=0, y=100)
btn1.place(x=60, y=100)
btn2.place(x=120, y=100)
btn3.place(x=0, y=158)
window.title("Pin Pad Machine")
window.geometry("230x295+250+250")
window.mainloop()

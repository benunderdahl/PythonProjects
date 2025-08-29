import tkinter

window = tkinter.Tk()

window.title("GUI Program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label")
my_label.pack()
window.mainloop()
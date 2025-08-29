from tkinter import *

def calculate():
    miles = int(input_text.get())
    km = miles * 1.609
    answer_box.config(text=f"{km}")


root = Tk()
root.title("Mi to Km Calculator")
root.config(padx=20, pady=40)

# left box
label_left = Label(root, text="is equal to", height=10, width=10)
label_left.grid(row=1, column=0)

# Text box top center
input_text = Entry(root, width=8)
input_text.grid(column=1, row=0)

# center box for displaying answer
answer_box = Label(root, text="0")
answer_box.grid(column=1, row=1)

#calculate button
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)

#top right label
mi_label = Label(root, text="Mi")
mi_label.grid(column=2, row=0)

# right center label
km_label = Label(root, text="Km")
km_label.grid(column=2, row=1)



root.mainloop()
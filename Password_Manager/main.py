from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip

FONT = ("Arial", 12,"bold")
NAVY = "#5D688A"
PEACH = "#F7A5A5"
YELLOW = "#FFDBB6"
PASTEL = "#FFF2EF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_text.delete(0, END)
    generated_password = password_generator.create_password()
    pyperclip.copy(generated_password)
    password_text.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if not website or not email or not password:
        messagebox.showerror(title="Emtpy Fields", message="Do not leave any empty fields")
    else:
        can_add = messagebox.askokcancel(title=website, message=f"Add this entry?\n"
                                                    f"Email: {email}\n"
                                                    f"Password: {password}\n"
                                                    f"Yes/No")
    if can_add:
        with open("data.txt", "a") as file:
            file.write(f"{website}   |   {email}   |   {password}\n")
        website_text.delete(0, END)
        email_text.delete(0, END)
        password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=NAVY)
canvas = Canvas(window, height=200, width=200, bg=NAVY, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

################### text fields #############################
website_text = Entry(window, width=35, bg=PASTEL)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

email_text = Entry(window, width=35, bg=PASTEL)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "example@email.com")

password_text = Entry(window, width=21, bg=PASTEL)
password_text.grid(row=3, column=1)

################### labels #############################
website_label = Label(text="Website:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
password_label.grid(row=3, column=0)

################### buttons #############################
generate = Button(text="Generate Password", bg=PEACH, fg=YELLOW, command=generate_password, width=14)
generate.grid(row=3, column = 2)

add_button = Button(text="Add", width=36, pady=10, bg=PEACH, fg=YELLOW, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json

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

#------------------------------ SEARCH FUNCTION -------------------------------#
def search_info():
    website = website_text.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("There is no Save File")
    else:
        if website in data:
            items = data[website]
            email = items["email"]
            password = items["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showerror(title="website now found", message=f"Was not able to find information for {website}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {website: {
            "email": email,
            "password": password
    }}

    if not website or not email or not password:
        messagebox.showerror(title="Emtpy Fields", message="Do not leave any empty fields")
    else:
        can_add = messagebox.askokcancel(title=website, message=f"Add this entry?\n"
                                                    f"Email: {email}\n"
                                                    f"Password: {password}\n"
                                                    f"Yes/No")
    if can_add:
        try:
            with open("data.json", "r") as file:
                print(new_data)
                data = json.load(file)
        except FileNotFoundError as e:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_text.delete(0, END)
            email_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=NAVY)
canvas = Canvas(window, height=200, width=200, bg=NAVY, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

################### text fields #############################
website_text = Entry(window, width=30, bg=PASTEL)
website_text.grid(row=1, column=1, sticky="w")
website_text.focus()

email_text = Entry(window, width=30, bg=PASTEL)
email_text.grid(row=2, column=1, sticky="w")
email_text.insert(0, "example@email.com")

password_text = Entry(window, width=25, bg=PASTEL)
password_text.grid(row=3, column=1, sticky="w")

################### labels #############################
website_label = Label(text="Website:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
website_label.grid(row=1, column=0, sticky="w")

username_label = Label(text="Email/Username:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
username_label.grid(row=2, column=0, sticky="w")

password_label = Label(text="Password:", font=FONT, pady=10, bg=NAVY, fg=YELLOW)
password_label.grid(row=3, column=0, sticky="w")

################### buttons #############################
search_button = Button(text="Search", width=7, bg=PEACH, fg=YELLOW, command=search_info)
search_button.grid(row=1, column=2, sticky="w")

generate = Button(text="Generate Password", bg=PEACH, fg=YELLOW, command=generate_password)
generate.grid(row=3, column = 2, sticky="w")

add_button = Button(text="Add", width=36, pady=10, bg=PEACH, fg=YELLOW, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")





window.mainloop()
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, padx=20, pady=20)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

mail = Label(text="Email/Username:")
mail.grid(row=2, column=0)

mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

get_password_but = Button(text="Generate Password")
get_password_but.grid(row=3, column=2)

add = Button(text="Add", width=14)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()

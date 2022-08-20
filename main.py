from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    username = user_input.get()
    password = pass_input.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"Confirm details: \nWebsite: {website}\nUsername: {username}\nPassword: {password}\nProceed to save?")
        if is_ok:
            total_data = website + ' | ' + username + ' | ' + password + '\n'
            with open("data.txt", 'a') as file:
                file.write(total_data)
                website_input.delete(0, 'end')
                pass_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)
# canvas
canvas = Canvas(height=200, width=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
# inputs
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()
user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2, sticky="EW")
user_input.insert(0, "cshikhar15@gmail.com")
pass_input = Entry(width=21)
pass_input.grid(row=3, column=1, sticky="EW")
# buttons
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)
add_pass = Button(text="Add Password", command=save_data, width=36)
add_pass.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()

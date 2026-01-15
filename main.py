from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password_action():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password = password_numbers + password_symbols + password_letters
    shuffle(password)
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)

# ---------------------------- SEARCH TOOL --------------------------------- #
def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='Entry not found.')
    else:
        website_name = website_input.get()
        if website_input.get() in data:
            messagebox.showinfo(title=website_name, message=f'''
Email: {data[website_name]['email']}
Password: {data[website_name]['password']}''')

        else:
            messagebox.showinfo(title='Error', message='Entry not found.')


#
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if password == '' or website == '' or email == '':
        messagebox.showinfo(title='Oopsie daisy', message="Don't leave any of the fields empty!")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            if messagebox.askokcancel(title=website,
                                      message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?'):
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:
            if messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?'):
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='black')

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:', fg='white',  bg='black')
website_label.grid(row=1, column=0)

email_label = Label(text='E-mail/Username:', fg='white', bg='black')
email_label.grid(row=2, column=0)

password_label = Label(text='Password', fg='white',  bg='black')
password_label.grid(row=3, column=0)

website_input = Entry(bg='black', fg='white', insertbackground='white')
website_input.focus()
website_input.grid(sticky="EW", row=1, column=1, columnspan=1, padx=2, pady=1)

email_input = Entry(bg='black', fg='white', insertbackground='white')
email_input.grid(sticky="EW", row=2, column=1, columnspan=2, padx=2, pady=1)
email_input.insert(END, 'gbnunes2000@gmail.com')

password_entry = Entry(bg='black', fg='white', insertbackground='white')
password_entry.grid(sticky="EW", row=3, column=1, padx=2, pady=1)

generate_password = Button(text='Generate Password', bg='black', fg="white", command=generate_password_action)
generate_password.grid(sticky="EW", row=3, column=2, padx=2, pady=1)

add_button = Button(text='Add', width=35, fg="white", bg='Black', command=save)
add_button.grid(sticky="EW", row=4, column=1, columnspan=2, padx=2)

search_button = Button(text='Search', fg='white', bg='black', command=search)
search_button.grid(sticky='EW', row=1, column=2, padx=2, pady=1)

window.mainloop()

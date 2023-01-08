from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_numbers + password_symbols + password_letters
  random.shuffle(password_list)

  passw = ""
  for char in password_list:
    passw += char

  password.delete(0, END)
  password.insert(0, passw)
  pyperclip.copy(passw)


def save_info():
  the_website = website.get()
  print(the_website)
  the_email = email.get()
  the_password = password.get()
  if the_website == '' or the_email == '' or the_password == '':
    messagebox.showinfo("Oops", "Please don't leave any field empty.")
  else:
    messagebox.askokcancel(title=website, message=f"this are the details entered: \nEmail: {email.get()} \nPassword: {password.get()} \nIs it okay to save?")
    line = f"{the_website} | {the_email} | {the_password}\n"
    with open("my_passwords.txt", 'a') as file:
      file.write(line)
      website.delete(0, END)
      password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
logo_img = canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", padx=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
website.focus()

email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "biruhtesfaye@gmail.com")

password = Entry(width=21)
password.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save_info)
add.grid(column=1, row=4, columnspan=2)




window.mainloop()
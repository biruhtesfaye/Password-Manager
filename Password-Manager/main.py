# Password Generator Project

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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

  new_data = {
    the_website: {
      "email": the_email,
      "password": the_password
    }
  }

  if the_website == '' or the_email == '' or the_password == '':
    messagebox.showinfo("Oops", "Please don't leave any field empty.")
  else:
    messagebox.askokcancel(title=website, message=f"this are the details entered: \nEmail: {email.get()} \nPassword: {password.get()} \nIs it okay to save?")
    line = f"{the_website} | {the_email} | {the_password}\n"
    try:
      with open("data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data)
    except:
      data = new_data
    finally:
      with open("data.json", 'w') as data_file:
        json.dump(data, data_file, indent=4)
        # file.write(line)
        website.delete(0, END)
        password.delete(0, END)

def search():
  the_website = website.get()
  try:
    with open("data.json", 'r') as data_file:
      data = json.load(data_file)
      if the_website in data:
        print("Yeah we got it.")
        element = data[the_website]
        the_email = element["email"]
        the_password = element["password"]
        print(the_password)
        messagebox.showinfo(title="We got it!", message=f"Email: {the_email}\nPassword: {the_password}")
      else:
        messagebox.showerror(title="Not found!", message=f"Sorry, there is password information associated with {the_website}")
  except:
    messagebox.showerror(title="Not found!", message="No Data File Found")

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

website = Entry(width=30)
website.grid(column=1, row=1, columnspan=2)
website.focus()

search = Button(text="Search", command=search, padx=15)
search.grid(column=2, row=1)

email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "placeholder-email@gmail.com")

password = Entry(width=21)
password.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save_info)
add.grid(column=1, row=4, columnspan=2)




window.mainloop()

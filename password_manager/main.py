from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

label_font = ("courier", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_func():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    new_data = {
        website:{
            "password":password,
            "email":email
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showerror(message="Please don't leave any field empty.")
    else:      
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file)
        else: 
            data.update(new_data) 
            with open("data.json" ,"w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
        
#----------------------------- Search ---------------------------------#

def search():
    website = website_entry.get()
    try: 
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="No such data.")
    else: 
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(message="No such data.")
    
    


# ---------------------------- UI SETUP ------------------------------- #


wn = Tk()
wn.config(padx=50, pady=50)
wn.title("Password Generator")


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)

#---The Labels---
website_label = Label(text="Website:", font=label_font)
email_label = Label(text="Email/Username:", font=label_font)
password_label = Label(text="Password:", font=label_font)

#---The Entries---
website_entry = Entry(width=30)
website_entry.focus()

email_entry = Entry(width=49)
email_entry.insert(0, "Aimal@gmail.com")
password_entry = Entry(width=30)

#---The Buttons---
generate_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", width=41, command=add_func)
search_btn = Button(text="Search", command=search, width=15)


#---Grid System ---
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

generate_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn.grid(row=1, column=2)


wn.mainloop()

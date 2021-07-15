import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

FONT_NAME = 'Courier'
BACKGROUND_COLOUR = 'Navy'
FOREGROUND_COLOUR = 'Snow'
MY_EMAIL = ''
SAVE_FILE = 'password_vault.txt'



def main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def gen_button_action():
        print("Generating password...")
        #Password Generator Project
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []
        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)

        password = "".join(password_list)
        pyperclip.copy(password)
        print(f"Your generated password is: {password}")
        pass_entry.insert(0, password)


    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def add_button_action():
        print("Saving password...")
        website = website_entry.get()
        user = user_entry.get()
        password = pass_entry.get()
        store_string = f"{website} | {user} | {password}\n"

        if len(website) == 0 or len(user) == 0 or len(password) == 0:
                messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} \nPassword: {password} \nIs it ok to save?")
            if is_ok:
                with open(SAVE_FILE, 'a') as f:
                    f.write(store_string)
                    website_entry.delete(0, END)
                    pass_entry.delete(0, END)

                print("Saved password!")
            else:
                print("Password not saved")

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=20, bg=BACKGROUND_COLOUR)

    # canvas for image
    canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOUR, highlightthickness=0)
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)


    # website label
    label_1 = Label(text="Website:", font=(FONT_NAME, 8), bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR)
    label_1.grid(column=0, row=1)

    # website entry
    website_entry = Entry(width=55, bg=FOREGROUND_COLOUR)
    website_entry.focus()
    #Gets text in entry
    print(website_entry.get())
    website_entry.grid(column=1, row=1, columnspan=2)

    # email/username label
    label_2 = Label(text="Email/Username:", font=(FONT_NAME, 8), bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR)
    label_2.grid(column=0, row=2)

    # email/user entry
    user_entry = Entry(width=55, bg=FOREGROUND_COLOUR)
    user_entry.insert(0, MY_EMAIL)
    #Gets text in entry
    print(user_entry.get())
    user_entry.grid(column=1, row=2, columnspan=2)

    # password label
    label_3 = Label(text="Password:", font=(FONT_NAME, 8), bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR)
    label_3.grid(column=0, row=3)

    # password entry
    pass_entry = Entry(width=33, bg=FOREGROUND_COLOUR)
    #Gets text in entry
    print(pass_entry.get())
    pass_entry.grid(column=1, row=3)

    # Generate button
    gen_button = Button(text="Generate Password", command=gen_button_action, highlightthickness=0, font=(FONT_NAME, 8))
    gen_button.grid(column=2, row=3)

    # Add button
    add_button = Button(text="Add", command=add_button_action, highlightthickness=0, font=(FONT_NAME, 8),
                        width=46)
    add_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()

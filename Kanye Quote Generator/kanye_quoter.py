import requests
from tkinter import *
from PIL import Image, ImageTk

def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]

    # write this on the canvas
    canvas.itemconfig(quote_text, text=f'{quote}')


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
img = Image.open("background.png")
background_img = ImageTk.PhotoImage(img)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye = Image.open("kanye.png")
kanye_img = ImageTk.PhotoImage(kanye)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()

import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")


dice = ["1.png","2.png","3.png","4.png","5.png","6.png"]
Image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
Image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=Image1)
label2 = tk.Label(window, image=Image2)

label1.image= Image1
label1.image = Image2       

label1.place(x=110, y=100)
label2.place (x=320 , y=100)

def roll_dice():
    Image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = Image1)
    label1.image = Image1

    Image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = Image2)
    label2.image = Image2

button = tk.Button(window, text="ROLL", bg="black", fg="white",font="Times 20 bold", command=roll_dice)
button.place(x=210, y=0)

window.mainloop()



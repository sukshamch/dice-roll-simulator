import tkinter as tk
from PIL import Image, ImageTk
import random
window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roller")

dice = ("E:/dice/dice1.jpg","E:/dice/dice2.jpg",
        "E:/dice/dice3.jpg","E:/dice/dice4.jpg",
        "E:/dice/dice5.jpg","E:/dice/dice6.jpg"
        )
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=40, y=100)
label2.place(x=300, y=100)
def dice_roll():
  image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
  label1.configure(image = image1)
  label1.image = image1

  image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
  label2.configure(image = image2)
  label2.image = image2



button = tk.Button(window,text="ROLL",bg="black",fg="green",command=dice_roll)
button.place(x =230, y = 0)
window.mainloop()
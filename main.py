import requests
from tkinter import *

qoute = "I AM THE GREATEST THERE AIN'T NO DEBATEST"
window = Tk()
window.title("THE GREATEST NO ONE CAN DEBATEST")
window.config(bg="white",padx=60,pady=60)

#Define Function
def change_qoute():
    global qoute
    data = requests.get(url="https://api.kanye.rest").json()
    qoute = data['quote']
    canvas.itemconfig(ct,text=qoute)

#Creating canvas and kanye qoute
canvas = Canvas(width=300,height=414,background="white",highlightthickness=0)
bubble = PhotoImage(file="background.png")
canvas.create_image(150,207,image=bubble)
canvas.grid(row=0,column=0)
ct = canvas.create_text(150,207,text=qoute,font=("Arial",30,"normal"),width=250)


#Creating Button
kanye =PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye,background="white",highlightthickness=0,bd=0,command=change_qoute)
kanye_button.grid(column=0,row=1)

window.mainloop()
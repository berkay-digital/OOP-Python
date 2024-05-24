import tkinter as tk


def button_click():
    print("I got clicked!")
    label1.config(text="You said: " + entry1.get())


window = tk.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.configure(background="black")

label1 = tk.Label(text="Type something", font=("Arial", 24, "bold"))
label1.pack()

entry1 = tk.Entry()
entry1.pack()

button1 = tk.Button(text="Click me!")
button1.pack()
button1.config(command=button_click)

image1 = tk.PhotoImage(file="test.png")
image1 = image1.subsample(2, 2)

label2 = tk.Label(image=image1)
label2.pack()

window.mainloop()

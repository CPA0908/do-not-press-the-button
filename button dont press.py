import tkinter

window = tkinter.Tk()

button = tkinter.Button(window, text="Do not press this button.", width=60)

button.pack(padx=20, pady=10)

clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickCount == 2:
        button.configure(text="Gah! Next time, no more button.")
    elif clickCount == 3:
        button.configure(text="I really mean it this time. Stop. It.")
    elif clickCount == 4:
        button.configure(text="Fine. You know what? This time I really mean it. Click it and find out.")
    elif clickCount == 5:
        button.configure(text="Say goodbye to the button.")
    else:
        button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
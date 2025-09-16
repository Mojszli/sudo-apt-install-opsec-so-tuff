
# Press Esc or Ctrl+Q to close.

import tkinter as tk

def close(e=None):
    root.destroy()

root = tk.Tk()
root.title("Overlay")


root.overrideredirect(True)
root.attributes('-topmost', True)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}+0+0")

root.configure(bg='black')


label = tk.Label(
    root,
    text="KAPOFF",
    fg='red',
    bg='black',
    font=('Helvetica', 14, 'bold'),  
    justify='center'
)

texts = [
    "you nigga",
    "test1",
    "test1",
    "test1"
]
for line in texts:
    lbl = tk.Label(
        root,
        text=line,
        fg="red",
        bg="black",
        font=("Helvetica", 36, "bold")
    )
    lbl.pack()

label.pack(expand=True)

root.bind("<Escape>", close)   # | we wont be needin it soon.
root.bind("<Control-q>", close)# | 

root.mainloop()

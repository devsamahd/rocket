import tkinter as tk
from tkinter import filedialog, Text 
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        print(tempApps)

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title = "select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    
    for app in apps:
        tk.Label(frame, text=app, bg="black", fg = "green").pack()


def runApps():
    for app in apps:
        os.startfile(app)







root.title("Rocket by Samahd")

canvas = tk.Canvas(root, height="500", width = "500", bg="blue")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth = "0.8", relheight = "0.8", relx = "0.1", rely = "0.1")


tk.Button(root, text = "Open File", padx=10, pady=5, fg="white", bg="blue", command=addApp).pack()

tk.Button(root, text = "Run Apps", padx=10, pady=5, fg="white", bg="blue", command=runApps).pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
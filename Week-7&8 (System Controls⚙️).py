from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown /l")

def shutdown():
    os.system("shutdown /s /t 1")

root = Tk()
root.title("Shutdown App")
root.geometry("500x500")
root.config(bg="#1E90FF")  
root.resizable(False, False)


Label(
    root, text="System Control Panel",
    font=("Times New Roman", 24, "bold"),
    bg="#1E90FF", fg="white"
).pack(pady=20)


buttons = [
    ("Restart", restart),
    ("Restart (20s Delay)", restart_time),
    ("Log Out", log_out),
    ("Shutdown", shutdown)
]

for i, (text, cmd) in enumerate(buttons):
    Button(
        root,
        text=text,
        font=("Times New Roman", 18, "bold"),
        relief=RAISED,
        cursor="hand2",
        command=cmd,
        bg="white", fg="black",
        activebackground="#4682B4"
    ).pack(pady=15, ipadx=20, ipady=5)

root.mainloop()

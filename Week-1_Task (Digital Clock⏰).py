from tkinter import *
from time import strftime

# Create the root window
root = Tk()
root.title("Digital Clock")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # 24-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Configure label style
label = Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')

# Call the time function
time()

# Run the GUI loop
root.mainloop()

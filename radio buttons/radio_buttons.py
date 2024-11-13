import tkinter as tk
from tkinter import messagebox

#function

def check_option():
    list=[]
    if red_option.get():
        list.append("Red Option")
    if green_option.get():
        list.append("Green Option")
    if blue_option.get():
        list.append("Blue Option")
    
    messagebox.showinfo("Option Selected",f"Radio button selected is {colour_option.get()}, the Checkbox selected is {list}")

#window

window=tk.Tk()
window.geometry("500x500")
window.title("Radio Buttons")

#special variable (STRINGVAR)
colour_option=tk.StringVar(value="Red")

#special variable (BOOLEANVAR)
red_option=tk.BooleanVar(value=False)
green_option=tk.BooleanVar(value=False)
blue_option=tk.BooleanVar(value=False)

#radio buttons
red=tk.Radiobutton(window, text="Red",variable=colour_option,value="Red")
red.pack()

green=tk.Radiobutton(window, text="Green",variable=colour_option,value="Green")
green.pack()

blue=tk.Radiobutton(window, text="Blue",variable=colour_option,value="Blue")
blue.pack()

#checkboxes

redcheckbox=tk.Checkbutton(window, text="Red Option", variable=red_option)
redcheckbox.pack()

greencheckbox=tk.Checkbutton(window, text="Green Option", variable=green_option)
greencheckbox.pack()

bluecheckbox=tk.Checkbutton(window, text="Blue Option", variable=blue_option)
bluecheckbox.pack()

#button

button=tk.Button(window,text="Press here to check", command=check_option)
button.pack()

window.mainloop()
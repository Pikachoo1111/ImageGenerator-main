import tkinter
import subprocess
#import generateimage.py
#import EncoderDecoder.py

root = tkinter.Tk()
def setup():
    root.title("Airplane Display")
    root.geometry("1920x600")
    root.configure(bg="white")
    root.resizable(False, False)
    label = tkinter.Label(root, text="Airplane Display", font=("Arial", 24), bg="black")
    label.place(x=960, y=50)
    label.pack()
    button = tkinter.Button(root, text="Generate Image", font=("Arial", 24), bg="white")
    button.pack()
    
setup()
root.mainloop()
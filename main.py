import tkinter
import subprocess
import urllib as url
from PIL import Image
#import generateimage.py
#import EncoderDecoder.py

file_path = "/Users/armaan/Downloads/ImageGenerator-main/generateimage.py"

root = tkinter.Tk()

def GenerateButton():
    global result1
    command = "python3 generateimage.py"
    result1 = subprocess.check_output(command, shell=True, text=True)
    url.urlretrieve(result1, "ai.png")
    picture = Image.open(result1)
    picture.save("picture.png")


def setup():
    root.title("Airplane Display")
    root.geometry("1920x600")
    root.configure(bg="white")
    root.resizable(False, False)
    label = tkinter.Label(root, text="Airplane Display", font=("Arial", 24), bg="black")
    label.place(x=960, y=150)
    label.pack()
    button = tkinter.Button(root, text="Generate Image", font=("Arial", 24), bg="white", command=GenerateButton)
    button.pack()
    


setup()
root.mainloop()
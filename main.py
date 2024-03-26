import tkinter
import subprocess
import urllib as url
from PIL import Image
import wget
#import generateimage.py
#import EncoderDecoder.py
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


file_path = "/Users/armaan/Downloads/ImageGenerator-main/generateimage.py"

root = tkinter.Tk()

def GenerateButton():
    global result1
    command = "python3 generateimage.py"
    result1 = subprocess.check_output(command, shell=True, text=True)
    wget.download(result1, "/Users/armaan/Downloads/Images")



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
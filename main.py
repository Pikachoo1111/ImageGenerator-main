import tkinter as tk
import subprocess
import urllib as url
from PIL import Image, ImageTk
import wget
#import generateimage.py
#import EncoderDecoder.py
import ssl
import os
import time

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


file_path = "/Users/armaan/Downloads/ImageGenerator-main/generateimage.py"

root = tk.Tk()

def GenerateButton():
    global result1
    command = "python3 generateimage.py"
    result1 = subprocess.check_output(command, shell=True, text=True)
    wget.download(result1, "/Users/armaan/Downloads/ImageGenerator-main/Images")
    image = Image.open("/Users/armaan/Downloads/ImageGenerator-main/Images/ai.png")
    resized_image = image.resize((500, 500))  # Resize the image to desired dimensions
    tk_image = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # Keep a reference to the image to prevent garbage collection
    label.pack()
    os.remove("/Users/armaan/Downloads/ImageGenerator-main/Images/ai.png")  # Remove the image after displaying it



    



def setup():
    root.title("Airplane Display")
    root.geometry("1920x600")
    root.configure(bg="white")
    root.resizable(False, False)
    label = tk.Label(root, text="Airplane Display", font=("Arial", 24), bg="black")
    label.place(x=960, y=150)
    label.pack()
    button = tk.Button(root, text="Generate Image", font=("Arial", 24), bg="white", command=GenerateButton)
    button.pack()
    


setup()
root.mainloop()
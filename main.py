import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import wget
import os
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Function to generate and display the image
def GenerateButton():
    global result1, label
    command = "python3 generateimage.py"
    result1 = subprocess.check_output(command, shell=True, text=True)
    wget.download(result1, "/Users/armaan/Downloads/ImageGenerator-main/Images")
    encodeImage("/Users/armaan/Downloads/ImageGenerator-main/Images/ai.png")
    image = Image.open("/Users/armaan/Downloads/ImageGenerator-main/Images/ai.png")
    resized_image = image.resize((500, 500))  # Resize the image to desired dimensions
    tk_image = ImageTk.PhotoImage(resized_image)
    label = tk.Label(frame, image=tk_image)
    label.image = tk_image  # Keep a reference to the image to prevent garbage collection
    label.pack()
    os.remove("/Users/armaan/Downloads/ImageGenerator-main/Images/ai.png")  # Remove the image after displaying it

# Function to encode image
def encodeImage(filepath):
    global result2
    command = "python3 EncoderDecoder.py -e " + filepath
    result2 = subprocess.check_output(command, shell=True, text=True)
    return result2

# Create the Tkinter window
root = tk.Tk()

# Create a canvas with scrollbar
canvas = tk.Canvas(root, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Function to adjust scroll region
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)

# Set up the UI
label_title = tk.Label(frame, text="Images", font=("Arial", 32), bg="black", fg="white")
label_title.pack(pady=20)

button_generate = tk.Button(frame, text="Generate Image", font=("Arial", 18), bg="white", command=GenerateButton)
button_generate.pack(pady=20)

# Configure the window
root.geometry("800x600")
root.resizable(False, False)

# Start the main event loop
root.mainloop()

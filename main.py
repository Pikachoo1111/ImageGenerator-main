import tkinter
import subprocess
#import generateimage.py
#import EncoderDecoder.py

file_path = "/Users/armaan/Downloads/ImageGenerator-main/generateimage.py"

root = tkinter.Tk()

def GenerateButton():
    command = "python3 generateimage.py"
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)

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
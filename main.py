import tkinter
import subprocess
#import generateimage.py
#import EncoderDecoder.py

file_path = "/Users/armaan/Downloads/ImageGenerator-main/generateimage.py"

root = tkinter.Tk()
def setup():
    root.title("Airplane Display")
    root.geometry("1920x600")
    root.configure(bg="white")
    root.resizable(False, False)
    label = tkinter.Label(root, text="Airplane Display", font=("Arial", 24), bg="black")
    label.place(x=960, y=150)
    label.pack()
    button = tkinter.Button(root, text="Generate Image", font=("Arial", 24), bg="white")
    button.pack()
    

def GenerateButton():
    completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
    if completed_process.returncode == 0:
        print("Execution successful.")
        print("Output:")
        print(completed_process.stdout)
setup()
root.mainloop()
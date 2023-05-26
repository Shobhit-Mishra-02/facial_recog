import tkinter as tk
from tkinter import filedialog
from modules.faceDetection import detectFace
import cv2
from PIL import Image, ImageTk

def display_image(image):
    # Convert the image from BGR to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a PIL Image from the RGB image array
    pil_image = Image.fromarray(image)

    # Convert the PIL Image to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(pil_image)

    # Create a Label widget to display the image
    image_label = tk.Label(window, image=tk_image)
    image_label.pack()

def select_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    img = detectFace(file_path)
    display_image(img)

# Create the Tkinter window
window = tk.Tk()
window.title("Facial detection program")
window.geometry("400x400")

# Create a label for the heading
heading_label = tk.Label(window, text="Program", font=("Arial", 16))
heading_label.pack(pady=20)

# Create a button to select the file
select_button = tk.Button(window, text="Select File", command=select_file)
select_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

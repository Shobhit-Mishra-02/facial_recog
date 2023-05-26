import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from modules.faceDetection import detectFace
from modules.eyeDetection import detectEye
import cv2

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

def select_image_for_faceDetection():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        img = detectFace(file_path)

        # Convert the image from BGR to RGB format
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Create a PIL Image from the RGB image array
        pil_image = Image.fromarray(image)

        # Convert the PIL Image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(pil_image)
        
        image_label.configure(image=tk_image)
        image_label.image = tk_image

def select_image_for_eyeDetection():
    file_path = filedialog.askopenfilename()
    if file_path:
        # print("Selected file:", file_path)
        img = detectEye(file_path)

        # Convert the image from BGR to RGB format
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Create a PIL Image from the RGB image array
        pil_image = Image.fromarray(image)

        # Convert the PIL Image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(pil_image)
        
        image_label.configure(image=tk_image)
        image_label.image = tk_image


# Create the Tkinter window
window = tk.Tk()
window.title("Facial detection")

# adding heading
heading_label = tk.Label(window, text="Human Facial Feature detection", font=("Arial", 16))
heading_label.pack(pady=20)

# Create a button to select the image
select_button = tk.Button(window, text="Detect Faces", command=select_image_for_faceDetection)
select_button.pack(pady=10)

select_button = tk.Button(window, text="Detect Eyes", command=select_image_for_eyeDetection)
select_button.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Start the Tkinter event loop
window.mainloop()

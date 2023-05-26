import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from modules.faceDetection import detectFace
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

def select_image():
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


# Create the Tkinter window
window = tk.Tk()
window.title("Facial detection")
# window.geometry("")

# Create a button to select the image
select_button = tk.Button(window, text="Detect Faces", command=select_image)
select_button.pack(pady=10)

select_button = tk.Button(window, text="Detect Eyes", command=select_image)
select_button.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Start the Tkinter event loop
window.mainloop()

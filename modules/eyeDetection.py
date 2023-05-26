import cv2

def detectEye(filePath):

    # Load the Haar cascade XML file for eye detection
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    # Load the image
    image = cv2.imread(filePath)  # Replace with the path to your image file

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the image
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the eyes
    for (x, y, w, h) in eyes:
        cv2.putText(image, "Eye", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with detected eyes
    # cv2.imshow("Eye Detection", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return image

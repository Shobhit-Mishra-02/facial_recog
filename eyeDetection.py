import cv2

# Load the pre-trained eye detection cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the image
image = cv2.imread('face.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform eye detection
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with eye detections
cv2.imshow('Eyes Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

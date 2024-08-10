import cv2
import numpy as np
import os

# Load the pre-trained face detection classifier from OpenCV
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Directory to save detected face images
output_dir = 'detected_faces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to detect faces in an image
def detect_faces(img):
    # Convert the image to grayscale as face detection works better on grayscale images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    # If no faces are detected, return the original image
    if len(faces) == 0:
        return img, 0

    # For each detected face, draw a rectangle around it and save the face
    face_count = 0
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Draw a label with a background box
        label = f"Face {face_count + 1}"
        (label_width, label_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        cv2.rectangle(img, (x, y - label_height - 10), (x + label_width, y), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        # Save the detected face
        face_img = img[y:y+h, x:x+w]
        face_filename = os.path.join(output_dir, f"face_{face_count + 1}.jpg")
        cv2.imwrite(face_filename, face_img)
        
        face_count += 1
    
    return img, face_count

# Capture video from the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the camera
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Detect faces in the current frame
    frame, face_count = detect_faces(frame)

    # Add face count text to the frame
    face_count_text = f"Faces Detected: {face_count}"
    cv2.putText(frame, face_count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the frame with detected faces and face count
    cv2.imshow('Video Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

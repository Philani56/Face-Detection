# Face Detection 👁️

This project demonstrates a simple face detection application using OpenCV. It captures video from the default camera, detects faces in real-time, and draws rectangles around detected faces.

## Prerequisites 📋

Before running the project, ensure you have the following installed:

- **Python 3.x** 🐍
- **OpenCV library** (`cv2`) 📸
- **NumPy library** (`numpy`) 🔢

You can install the required libraries using pip:

- pip install opencv-python numpy

## Getting Started 🚀
1. Clone the Repository

If you're starting with a Git repository, clone it to your local machine:
git clone <[repository-url](https://github.com/Philani56/Face-Detection)>

2. Download Haar Cascade XML File
Ensure the Haar cascade XML file for face detection is available in your project directory.
If not, you can download it from the OpenCV GitHub repository:

Haar Cascade Frontal Face XML 🗂️

Save the file in the same directory as your script.

3. Run the Script
Execute the Python script to start the face detection:

- python face_detection.py

## Stopping the Program

To stop the program, press the 'q' key while the video window is active ⏹️.

### Troubleshooting 🛠️

- Camera Not Found:

- Ensure that your camera is connected and properly configured 📷.

### XML File Not Found:

- Verify that haarcascade_frontalface_default.xml is in the same directory as your script or provide the correct path 📂.

### Library Issues:

- Make sure the OpenCV and NumPy libraries are correctly installed. If you encounter any issues, try reinstalling them 🔄.

## License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

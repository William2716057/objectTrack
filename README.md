# Object Tracking with OpenCV
This project demonstrates object tracking using OpenCV's CSRT tracker. It can track an object from either a webcam feed or a video file.

## Prerequisites
Make sure you have the following libraries installed:
- OpenCV
- imutils
You can install them using pip:
```
pip install opencv-python opencv-contrib-python imutils
```

## Usage
1. Initialize the Tracker: The script uses the CSRT tracker from OpenCV.
2. Select the Video Source: Set the camera variable to True for using the webcam or False for using a video file (sample.mp4 by default).
3. Run the Script: The script will start and you will be prompted to select the object to track in the first frame.
4. Track the Object: The script will track the object across subsequent frames and draw a rectangle around it.
5. Exit: Press 'q' to exit the tracking and close the video window.

## Notes
- Ensure you have a video file named sample.mp4 in the same directory if you are not using the webcam or adjust to your own file.
- The script uses imutils for frame resizing for easier processing.

Feel free to modify the code as per your requirements, such as changing the tracker type or adding additional functionalities.

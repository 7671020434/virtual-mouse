# Virtual Mouse - Eye Control with Blink Detection

This is a **Virtual Mouse** project that allows you to control the mouse cursor using your eyes and trigger mouse clicks with blinks. The project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** for eye tracking and mouse interaction.

## Features

- **Eye Control**: Move the mouse cursor by moving your eyes.
- **Blink Detection**: Perform a left-click by blinking both eyes simultaneously.
- **Real-time Processing**: Uses webcam feed to track eyes and detect blinks in real-time.

## Technologies Used

- **OpenCV**: Used for capturing webcam feed and image processing.
- **MediaPipe**: Used for facial landmark detection, specifically to track the eyes.
- **PyAutoGUI**: Used for controlling the mouse cursor and performing mouse clicks.
- **Python**: The primary language used for implementing the project.

## Requirements

- Python 3.x
- Install the following dependencies using `pip`:

  ```bash
  pip install opencv-python mediapipe pyautogui

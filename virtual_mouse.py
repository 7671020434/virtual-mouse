import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Face Mesh and Webcam
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Get Screen Dimensions
screen_width, screen_height = pyautogui.size()

# Start Webcam
cap = cv2.VideoCapture(0)

# Variables to track blink state
last_blink_time = 0
blink_duration_threshold = 0.3  # Time threshold for blink detection (in seconds)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Mirror the image
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_img)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get the coordinates of the eyes (left and right)
            left_eye_top = face_landmarks.landmark[159]
            left_eye_bottom = face_landmarks.landmark[23]
            right_eye_top = face_landmarks.landmark[386]
            right_eye_bottom = face_landmarks.landmark[253]
            
            # Convert normalized coordinates to pixel values
            left_eye_top_y = int(left_eye_top.y * screen_height)
            left_eye_bottom_y = int(left_eye_bottom.y * screen_height)
            right_eye_top_y = int(right_eye_top.y * screen_height)
            right_eye_bottom_y = int(right_eye_bottom.y * screen_height)

            # Calculate the vertical distance between top and bottom eyelids for each eye
            left_eye_height = abs(left_eye_top_y - left_eye_bottom_y)
            right_eye_height = abs(right_eye_top_y - right_eye_bottom_y)

            # Blink detection logic
            if left_eye_height < 20 and right_eye_height < 20:  # Threshold for blink detection
                if time.time() - last_blink_time > blink_duration_threshold:
                    # Trigger mouse click event
                    pyautogui.click()
                    last_blink_time = time.time()  # Update last blink time

            # Draw landmarks for visual feedback
            mp_drawing.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)
            
            # Get eye position to move the cursor
            left_eye = face_landmarks.landmark[33]  # Left eye center
            right_eye = face_landmarks.landmark[263]  # Right eye center
            
            # Convert normalized coordinates to pixel values
            left_eye_x = int(left_eye.x * screen_width)
            left_eye_y = int(left_eye.y * screen_height)
            right_eye_x = int(right_eye.x * screen_width)
            right_eye_y = int(right_eye.y * screen_height)

            # Average the positions of both eyes to get the cursor position
            x = (left_eye_x + right_eye_x) // 2
            y = (left_eye_y + right_eye_y) // 2

            # Move Mouse
            pyautogui.moveTo(x, y)

    cv2.imshow("Virtual Mouse - Eye Control with Blink Click", img)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

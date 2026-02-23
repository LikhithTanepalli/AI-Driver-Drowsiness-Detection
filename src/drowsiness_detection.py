import os
import cv2
import numpy as np
import threading
import pygame
import time
from tensorflow.keras.models import load_model

# ================= PATH HANDLING =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "drowsiness_eye_model.keras")
ALARM_PATH = os.path.join(BASE_DIR, "..", "alarm.wav")

# ================= LOAD MODEL =================

model = load_model(MODEL_PATH)
print("Model Loaded Successfully")

# ================= LOAD CASCADES =================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# ================= INIT ALARM =================

pygame.mixer.init()
pygame.mixer.music.load(ALARM_PATH)

def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

# ================= START WEBCAM =================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

score = 0
threshold = 10  # sensitivity

print("AI Driver Monitor Started")
print("Press Q to Quit")

# ================= MAIN LOOP =================

while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # -------- UI HEADER PANEL --------
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (500, 120), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status_text = "No Face Detected"
    status_color = (0, 255, 255)

    for (x, y, w, h) in faces:

        face_color = frame[y:y+h, x:x+w]
        face_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_gray)
        eyes = sorted(eyes, key=lambda x: x[2]*x[3], reverse=True)[:2]

        for (ex, ey, ew, eh) in eyes:

            eye = face_color[ey:ey+eh, ex:ex+ew]

            try:
                eye = cv2.resize(eye, (64, 64))
                eye = eye / 255.0
                eye = np.reshape(eye, (1, 64, 64, 3))

                prediction = model.predict(eye, verbose=0)
                confidence = prediction[0][0]

                # Display confidence
                cv2.putText(frame, f"Confidence: {confidence:.2f}",
                            (10, 60),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.7,
                            (255, 255, 255), 2)

                if confidence < 0.4:
                    score += 1
                    status_text = "Eyes Closed"
                    status_color = (0, 0, 255)
                else:
                    score = 0
                    status_text = "Eyes Open"
                    status_color = (0, 255, 100)

            except:
                pass

        if score > threshold:
            status_text = "DROWSINESS ALERT!"
            status_color = (0, 0, 255)

            # Red border
            cv2.rectangle(frame,
                          (0, 0),
                          (frame.shape[1], frame.shape[0]),
                          (0, 0, 255),
                          8)

            threading.Thread(target=play_alarm).start()

    # -------- STATUS DISPLAY --------
    cv2.putText(frame, status_text,
                (10, 30),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                status_color, 2)

    # -------- PROGRESS BAR --------
    bar_width = min(score * 20, 250)
    cv2.rectangle(frame, (10, 90), (10 + bar_width, 110), (0, 0, 255), -1)
    cv2.rectangle(frame, (10, 90), (260, 110), (255, 255, 255), 2)

    # -------- FPS --------
    fps = 1 / (time.time() - start_time)
    cv2.putText(frame, f"FPS: {int(fps)}",
                (400, 30),
                cv2.FONT_HERSHEY_DUPLEX,
                0.7,
                (0, 255, 255), 2)

    # -------- FOOTER --------
    cv2.putText(frame, "AI Driver Monitor v1.0",
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_DUPLEX,
                0.6,
                (200, 200, 200), 1)

    cv2.imshow("AI Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
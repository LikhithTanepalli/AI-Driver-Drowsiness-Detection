# AI Driver Drowsiness Detection System 🚗💤

## 📌 Overview

The AI Driver Drowsiness Detection System is a real-time computer vision application designed to detect signs of driver drowsiness using a webcam. When prolonged eye closure is detected, the system triggers an audible alarm to alert the driver.

## 🎯 Problem

Driver fatigue and drowsiness are major causes of road accidents. This project aims to provide an affordable real-time monitoring system that can detect potential drowsiness and alert the driver before an accident occurs.

## 💡 Solution

The system uses a webcam to continuously monitor the driver's eyes. A trained deep learning model analyzes the captured eye images and determines whether the eyes indicate an alert or drowsy state.

When drowsiness is detected for a sustained period, an alarm is triggered.

## ✨ Features

- Real-time webcam-based monitoring
- AI-based eye-state detection
- Automatic drowsiness detection
- Audible warning alarm
- Runs on a local computer
- Designed for real-time driver safety assistance

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pygame
- Computer Vision
- Convolutional Neural Network (CNN)

## 📂 Project Structure

```text
AI-Driver-Drowsiness-Detection/
│
├── model/              # Trained AI model
├── src/                # Source code
├── alarm.wav           # Warning alarm
├── requirements.txt    # Python dependencies
├── .gitignore          # Git configuration
└── README.md           # Project documentation


Webcam
   ↓
Capture Driver's Face/Eyes
   ↓
Eye Detection
   ↓
AI Model
   ↓
Alert / Drowsy Classification
   ↓
Drowsiness Detected?
   ↓
Trigger Alarm


git clone https://github.com/LikhithTanepalli/AI-Driver-Drowsiness-Detection.git



cd AI-Driver-Drowsiness-Detection






pip install -r requirements.txt






### 2. ⚠️ One thing before you click Commit

I don't want you to claim something that your actual code doesn't do.

The README above assumes your project uses **TensorFlow/Keras, OpenCV, NumPy, Pygame, CNN, webcam**, etc., based on the project you previously described. If any of those aren't actually in your code, **tell me before committing**, and I'll adjust it.

### 3. Then click **Commit changes...**

Top-right, the green button you can see.

Use the commit message:

> **Improve project documentation**

Then click **Commit changes**.

### 4. After committing

Go back to the main repository page. You should see your README displayed nicely underneath your files.

**Don't submit the Hacker House application yet.** 🚀

Next we'll check your repository structure and make sure the **actual source code is visible and runnable**, which is more important than just having a nice README.

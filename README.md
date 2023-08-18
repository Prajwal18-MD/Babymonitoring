# Baby Monitoring

This repository contains a Python script that detects emotions from facial expressions in images using computer vision techniques. The script leverages the `cv2` (OpenCV) and `dlib` libraries to carry out face detection and emotion analysis.

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Requirements](#requirements)


## Introduction

This script demonstrates how to predict emotions, such as "Laughing" or "Crying," based on facial expressions in images. It is designed as a simple example and starting point for understanding the process of emotion detection using computer vision tools.

## How It Works

1. **Face Detection (`detect_face` function)**:
   - The script loads an image using `cv2` (OpenCV) and converts it to grayscale.
   - It uses the Histogram of Oriented Gradients (HOG) face detector provided by the `dlib` library to detect faces in the image.
   - If a face is detected, the script extracts the face region from the grayscale image.

2. **Emotion Analysis (`analyze_emotion` function)**:
   - The script employs a Haar Cascade classifier to detect mouth regions in the face image.
   - If a mouth is detected, the script predicts that the person is "Laughing."
   - If no mouth is detected, the script predicts that the person is "Crying."

3. **Main Function (`main`)**:
   - The main function orchestrates the overall process.
   - Replace `'image'` in the `img_path` variable with your image's filename.
   - It calls the `detect_face` function to identify a face in the provided image.
   - If a face is detected, it calls the `analyze_emotion` function to predict the emotion based on the facial expression.
   - The predicted emotion is then printed to the console.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
## Install Dependencies
   - pip install opencv-python dlib

## Requirements
   - Python 3.x.
   - OpenCV (cv2) library.
   - dlib library.
   - Haar Cascade classifier XML file (haarcascade_frontalface_default.xml).

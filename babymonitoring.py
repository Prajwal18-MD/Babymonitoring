import cv2
import dlib

def detect_face(img_path):
    # Load the image
    img = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initialize the HOG face detector
    hog_detector = dlib.get_frontal_face_detector()

    # Detect faces in the image
    faces = hog_detector(gray_img)

    if len(faces) == 0:
        return None
    else:
        # dlib returns the bounding box coordinates of the detected faces
        (x, y, w, h) = (faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height())
        return gray_img[y:y + h, x:x + w]

def analyze_emotion(face_img):
    mouth_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Replace with the full path
    mouths = mouth_cascade.detectMultiScale(face_img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 10))

    if len(mouths) > 0:
        return "Laughing"
    else:
        return "Crying"

def main():
    img_path = 'image'  # Replace 'image.jpg' with your image filename
    face_img = detect_face(img_path)

    if face_img is not None:
        emotion = analyze_emotion(face_img)
        print("Predicted Emotion:", emotion)
    else:
        print("No face detected in the image.")

if __name__ == "__main__":
    main()

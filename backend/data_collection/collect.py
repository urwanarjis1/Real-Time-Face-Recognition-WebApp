import cv2
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def collect_data(person_name, num_samples=200):
    person_dir = os.path.join(config.DATASET_DIR, person_name)
    os.makedirs(person_dir, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(config.HAAR_PATH)
    cap = cv2.VideoCapture(0)

    count = 0
    while count < num_samples:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (config.IMG_SIZE, config.IMG_SIZE))
            path = os.path.join(person_dir, f"{count}.jpg")
            cv2.imwrite(path, face)
            count += 1
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"Samples: {count}/{num_samples}", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.imshow("Collecting Data", frame)
        if cv2.waitKey(1) == 27:  # ESC to stop
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter the person's name: ")
    collect_data(name)

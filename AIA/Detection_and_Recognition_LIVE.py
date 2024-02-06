import face_recognition
import cv2
import pickle
import numpy as np
import MarkAttendence
import os
from unlock import change_state, clean_gpio

print("[INFO] Loading Encodings ... ")
with open("Encodings/Encodings.dat", "rb") as f:
    data = pickle.load(f)


print("[INFO] Starting Camera ... ")
video_capture = cv2.VideoCapture(0, cv2.CAP_V4L)

MarkAttendence.getjsonDetails()
MarkAttendence.checkIfCsvExist()

face_locations = []
face_encodings = []

process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)


    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Initialize face_distances outside the loop
    face_distances = []

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=1, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(data['encodings'], face_encoding)
            name = "Unknown"

            if data['encodings']:
                face_distances = face_recognition.face_distance(data['encodings'], face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = data['names'][best_match_index]
                    MarkAttendence.getCSVdata([name])
                    MarkAttendence.writeValuesInCSV()
                    change_state()

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
clean_gpio()
cv2.destroyAllWindows()

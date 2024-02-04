

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)

#Load Known faces
vishal_image = face_recognition.load_images_file("faces/vishal.jpg")
vishal_encoding = face_recognition.face_encoding(vishal_image)[0]
peeyush_image = face_recognition.load_image_file("faces/peeyush.jpg")
peeyush_encoding = face_recognition.face_encoding(peeyush_image)[0]

known_face_encodings = [vishal_encoding , peeyush_encoding]
known_face_names = ["vishal","peeyush"]

#list of expected students

face_locations = []
face_encodings = []

#Get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv","w+",newline="")
lnwriter = cv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resiSze(frame, (0,0), fx=0.25, ty=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGRA2BGR)

    #Recognize faces
    face_locations =

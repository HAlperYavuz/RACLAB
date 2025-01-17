import cv2
import imutils
import time
import numpy as np
import datetime

cap = cv2.VideoCapture(0)

cap.set(3, 1080)  # set width
cap.set(4, 1920)  # set height

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Kadin', 'Erkek']


def initialize_caffe_models():

    age_net = cv2.dnn.readNetFromCaffe(
        'model2/age.prototxt',
        'model2/age.caffemodel')

    gender_net = cv2.dnn.readNetFromCaffe(
        'model2/gender.prototxt',
        'model2/gender.caffemodel')

    return (age_net, gender_net)


def read_from_camera(age_net, gender_net):
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:

        ret, image = cap.read()

        face_cascade = cv2.CascadeClassifier('model2/haarcascade_frontalface_alt.xml')

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,8)

        if (len(faces) > 0):
            print("Found {} faces".format(str(len(faces))))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

            # Get Face
            face_img = image[y:y + h, h:h + w].copy()
            blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            blob1 = cv2.dnn.blobFromImage(face_img, 1, (224, 224), MODEL_MEAN_VALUES, swapRB=False)

            an = datetime.datetime.now()
            tarih = datetime.datetime.strftime(an, '%c')

            # Predict Gender
            gender_net.setInput(blob1)
            gender_preds = gender_net.forward()
            gender = gender_list[gender_preds[0].argmax()]
            print("Gender : " + gender)

            # Predict Age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = age_list[age_preds[0].argmax()]
            print("Age Range: " + age)
            print(tarih)

            overlay_text = "%s %s" % (gender, age)
            cv2.putText(image, overlay_text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    age_net, gender_net = initialize_caffe_models()

    read_from_camera(age_net, gender_net)





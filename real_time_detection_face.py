import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime, date
from imutils.video import VideoStream

today = date.today()

path = '../Project-Face_Recognition&Mask_Detection/AttendanceImages'

# Get images names from a folder
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


# Make encoding for images
def findEncodings(images1):
    encodeList = []
    for img in images1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)


# Record attendance of persons who appeared on webcam, then record them into csv file
def markAttendance(nom):
    with open('../Project-Face_Recognition&Mask_Detection/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
        nameList.append(entry[0])
        if nom not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            d1 = today.strftime("%d/%m/%Y")
            f.writelines(f'\n{nom},{dtString}, {d1}')


# Webcam function which make boundary box around a face
class DetectFace(object):
    def __init__(self):
        self.vs = VideoStream(src=0).start()
        self.cam = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        frame = self.vs.read()

        while True:
            imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if faceDis[matchIndex] < 0.50:
                    name = classNames[matchIndex].upper()
                    score = str(round(100 - faceDis[matchIndex] * 100, 2))
                    ps = name + ': ' + score
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, ps, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)
                else:
                    Uname = 'Unknown'
                    uy1, ux2, uy2, ux1 = faceLoc
                    uy1, ux2, uy2, ux1 = uy1 * 4, ux2 * 4, uy2 * 4, ux1 * 4
                    cv2.rectangle(frame, (ux1, uy1), (ux2, uy2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (ux1, uy2 - 35), (ux2, uy2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, Uname, (ux1 + 6, uy2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(Uname)
                    # width, height = 250, 350
                    # pts1 = np.float32(
                    #     [[ux1 - 10, uy1 - 10], [ux2 - 10, uy1 - 10], [ux1 + 10, uy2 + 10], [ux2 + 10, uy2 + 00]])
                    # pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
                    # matrix = cv2.getPerspectiveTransform(pts1, pts2)
                    # imgOutput = cv2.warpPerspective(img, matrix, (width, height))
                    # data = im.fromarray(imgOutput)
                    # data.save('C:/Users/khale/OneDrive/Desktop/Django_detction_face/screenshot/pic' + str(k) + '.png')
                    # k = k+1
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

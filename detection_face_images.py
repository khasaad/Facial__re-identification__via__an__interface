from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import cv2


chris_hemsworth_image = face_recognition.load_image_file("../Project-Face_Recognition&Mask_Detection/Images"
                                                         "/chris_hemsworth.jpg")
chris_hemsworth_face_encodings = face_recognition.face_encodings(chris_hemsworth_image)[0]

jeremy_renner_image = face_recognition.load_image_file("../Project-Face_Recognition&Mask_Detection/Images"
                                                       "/jeremy_renner.jpg")
jeremy_renner_face_encodings = face_recognition.face_encodings(jeremy_renner_image)[0]

known_face_encodings = [chris_hemsworth_face_encodings, jeremy_renner_face_encodings]
known_face_names = ["chris_hemsworth", "jeremy_renner"]

list_names = []


def load_image(img):
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    list_names = []

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        # faceDis = face_recognition.face_distance(known_face_encodings, face_encoding)
        # matchIndex = np.argmin(faceDis)
        # score = faceDis[matchIndex]

        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            # print(first_match_index)
            name = known_face_names[first_match_index]
            list_names.append(name)

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height), (right, bottom)), fill=(0, 255, 0), outline=(0, 255, 0))
        draw.text((left, bottom - text_height), name, fill=(255, 255, 255, 255))

    with open('../Project-Face_Recognition&Mask_Detection/names.csv', 'w') as f:
        # f.truncate()
        for nom in list_names:
            f.write(nom)
            f.write('\n')
    # return pil_image
    pil_image.save('static/images/show.jpg')

    # del draw
    # pil_image.show()


# load_image("../Project-Face_Recognition&Mask_Detection/Images/group.jpg")

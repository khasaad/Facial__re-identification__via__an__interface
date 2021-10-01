from flask import Flask, flash, Response, render_template, redirect, request, url_for
from real_time_detection_face import DetectFace
from detect_mask_video import MaskDetect
import jinja2
import os
import pandas as pd
from detection_face_images import load_image
import sqlite3

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True

UPLOAD_FOLDER = 'static/images/'

app.secret_key = "khaled_saad"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

df = pd.read_csv('Attendance.csv')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    template = jinja_env.get_template('homepage.html')
    return template.render()


@app.route('/getImages')
def home():
    return render_template("index.html")


@app.route('/getImages', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):

        load_image(file)

        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename='show.jpg')
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/getImages/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename), code=301)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(DetectFace()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed/about_faces', methods=("POST", "GET"))
def html_table():
    return render_template('simple.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/mask_feed')
def mask_feed():
    return Response(gen(MaskDetect()), mimetype='multipart/x-mixed-replace; boundary=frame')


connection = sqlite3.connect('database.db', check_same_thread=False)

if connection:
    print("Connected Successfully")
else:
    print("Connection Not Established")

cursor = connection.cursor()


@app.route('/getImages/getinformation')
def get_information():
    file1 = open('../Project-Face_Recognition&Mask_Detection/names.csv', 'r')
    names = list(file1.readlines())
    temp = ["name_client = '%s'" % str(name).strip() for name in names]
    print('names: ', names)
    print(temp)
    cursor.execute("SELECT * FROM identification where %s" % " OR ".join(temp))

    rows = cursor.fetchall()
    print('rows -------------->', rows)

    return render_template("example.html", rows=rows)


if __name__ == '__main__':
    app.run()

<h1>Facial re-identification via an interface</h1>
<img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/opencv.png'>

Key words: Computer Vision, OpenCV, dlib, face recognition, SVM, Flask.

<h2>Introduction</h2>
<p>A chain of nightclubs wants to build up and use a file of its customers. This company wants to implement a system that will be able to scan the faces of its customers to link them to a history (attendance, violence, over-consumption, ...) and also the face detection must work for photos with a single individual or on a group of people.</p>
<p>This project consists of requesting information previously stored in a database (photos of faces) in order to detect faces, then making it available via an interface.</p>

<h2>Project components</h2>
<p>The project consists of three parts:</p>
<ul>
  <li>Detect mask</li>
  <li>Detect faces in real time</li>
  <li>Detect faces in an image</li>
</ul>

<h2>How to use</h2>
<ol>
  <li>Clone the github repo on your machine:<br><code>git clone https://github.com/khasaad/Facial__re-identification__via__an__interface.git</code></li>
  <li><code>pip install -r requirements.txt</code></li>
</ol>

<h2>Flask interface</h2>

<p>To display the interface:</p>
<ol>
  <li>In terminal, run: python from_data.py</li>
</ol>

<img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g1.PNG'>

<p>This interface contains a sidebar which can apply the three parts of the project: Images, Mask and Webcam.</p>

<ul>
  <li>Images: To detect faces in an image.</li>
  <p>Once we click on Images, another page will appear where we will add an image to detect faces.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g2.PNG'>
  <p>We add the image by clicking on Choose File, then we click on Apply.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g3.PNG'>
</ul>

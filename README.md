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
<p>In terminal, run:</p>

 <code> python from_data.py</code>

<p></p>
<img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g1.PNG'>

<p>This interface contains a sidebar which can apply the three parts of the project: Images, Mask and Webcam.</p>

<ul>
  <li>Images: To detect faces in an image.</li>
  <p>Once we click on Images, another page will appear where we will add an image to detect faces.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g2.PNG'>
  <p>We add the image by clicking on Choose File, then we click on Apply.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g3.PNG'>
  <p>As seen in the image above, we get the result where it detects known faces and other unknowns.</p>
  <p>Pour obtenir des informations sur les visages connus, on utilise le chemin suivant: "/getImages/getinformation" et le résultat va apparaître dans une page html.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g4.PNG'>
  <li>Mask: To detect who is wearing the mask or not.</li>
  <p>Once we click on Mask, a Webcam page will appear where we will detect the faces that wear the mask or not.</p>
  <li>Webcam: To detect faces in real time.</li>
  <p>Once you click on Webcam, a Webcam page will appear where we will detect people's faces if they are known with their name and score or if they are not known. Then with the    following path "/video_feed/about_faces" we can open another html page containing all current or previous information.</p>
  <img src='https://github.com/khasaad/Facial__re-identification__via__an__interface/blob/master/Images_git/g5.PNG'>
</ul>

<h3>References</h3>
<p>[1]<a href="https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/" target="_blank">OpenCV Face Recognition</a></p>
<p>[2]<a href="https://intellica-ai.medium.com/a-guide-for-building-your-own-face-detection-recognition-system-910560fe3eb7" target="_blank">A Guide for building your own Face Detection & Face Recognition system</a></p>
<p>[3]<a href="https://cmusatyalab.github.io/openface/" target="_blank">Open Face</a></p>
<p>[4]<a href="https://arsfutura.com/magazine/face-recognition-with-facenet-and-mtcnn/" target="_blank">Face Recognition with FaceNet and MTCNN</a></p>
<p>[5]<a href="https://ghaliahmed.wordpress.com/2018/10/13/abstract/" target="_blank">Face Detection and Recognition in Real-World Videos Using Deep Learning Method</a></p>
 

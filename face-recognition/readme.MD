# Face Recognition in Under 25 Lines of Python Code

## Python code for eye and face recognition

[Click here to read](https://medium.com/p/face-recognition-under-25-lines-of-code-with-python-da7ccfe610c3)

![image](https://miro.medium.com/max/700/0*pcSFw5imwQZFAzDY.jpg)

In this article, we will look at an amazingly simple way to get started with face recognition using Python and the OpenCV Open Library.

### What is OPEN CV?

OpenCV is the most popular computerized library. Originally written in C / C ++, it now provides Python binding.

OpenCV uses machine learning algorithms to search faces within an image. Because the face is so hard, there is not a single simple test that will tell you whether it got a face or not. Instead, there are thousands of smaller patterns and features that should go hand in hand. Algorithms break down face recognition into thousands of smaller, more sophisticated, easier-to-solve tasks. These functions are also called separation.
For some features such as faces, you may have 6,000 or more separate divisions, all of which must be face-to-face (within the limit of error, of course). But that’s where the problem lies: to find a face, the algorithm starts at the top left of the image and goes down across the small data blocks, looking at each block, asking, “Is this the face? … Is this the face? … Is this the face? “With 6,000 or more tests per block, you may have millions of calculations to do, which will grind your computer to a standstill.
Around this, OpenCV uses cascades. What is a cascade? A good answer can be found in the dictionary: “waterfall or series of waterfalls.”

Like a series of waterfalls, the OpenCV cascade cuts the problem of face detection in many stages. With each block, it performs a very difficult and fast test. When that passes, do a more detailed test, and so on. The algorithm can have 30 to 50 of these categories or cascades, and it will only get a face if all the categories pass.

The advantage is that most of the images will return a negative one among the first few sections, which means that the algorithm will not waste time testing all 6,000 elements in it. Instead of taking hours, facial recognition can now be done in real-time.

### Installing OpenCV
I am going to install open cv via PIP.
```bash
pip install opencv-python
```

### Demo

![image](https://miro.medium.com/max/2400/1*UvfE_LrXVkeEt7ns8uroOA.gif)

### Code
#### Folder and file structure

![image](https://miro.medium.com/max/301/1*PtV2UglgXMjXqkK6hagZ8g.png)

### main.py

```python
## pip install opencv-python

import cv2 as cv

face_cascade = cv.CascadeClassifier("./lib/haarcascade_frontalface_default.xml")
face_cascade_eye = cv.CascadeClassifier("./lib/haarcascade_eye.xml")
# face_glass = cv.CascadeClassifier('./lib/haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture(0)
while cap.isOpened():

    falg, img = cap.read()  # start reading the camera output i mean frames
    # cap.read() returning a bool value and a frame onject type value

    gray = cv.cvtColor(
        img, cv.COLOR_BGR2GRAY
    )  # converting to grayscale image to perform smoother
    faces = face_cascade.detectMultiScale(
        img, 1.1, 7
    )  # we use detectMultiscale library function to detect the predefined structures of a face
    eyes = face_cascade_eye.detectMultiScale(img, 1.1, 7)
    # using for loops we are trying to read each and every frame and map
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

    for (a, b, c, d) in eyes:
        cv.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 1)

    cv.imshow("img", img)
    c = cv.waitKey(1)
    if c == ord("q"):
        break

cv.release()
cv.destroyAllWindows()
```

[Click here to download libraries and code](https://mega.nz/file/6qRGiBxY#MNnnZl5imYpRtBBe9-H9MpClrz8wNcuYhS1ELpMzXAM)

### How to run
Open a terminal in the project root and run python3 main.py this will launch a pop-up using your camera. Make sure that python3 is installed, if not checkout [install python](https://hackeradda.com/installing-python).

If you face any problems please feel free to comment.

Thank you.
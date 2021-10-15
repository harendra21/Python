# How to create a screen and webcam recorder using python
[Read here](https://medium.com/p/21c407277d42)
![image](https://cdn-images-1.medium.com/max/800/1*ebYm1JJrI5IqyKxjukBb7g.jpeg) 

Create a smart screen recording software like `OBS studio` and `Camtasia with just 25 lines of python this is super easy super fun and super crazy.

So, to start with this project you will need python installed on our computer. We are going to use a python code editor called pycharm, and once this pycharm is ready we'll just hit this new project button and give our project a fancy name. It could be like a screen capture tool.

### install packages
We need total 3 packages to install
```bash
pip install pillow
pip install numpy
pip install opencv-contrib-python
```
It will take some time to install packages.

### Capturing The Screen

![image](https://cdn-images-1.medium.com/max/800/1*uV6SHKOnDD26NmKOGcamxA.jpeg)

So, to start capturing the screen we need to use PIL image grab and select the boundary which we want to capture by `bbox()` method. Then we have to convert these image points to `numpy` array and then pass these image arrays to open cv2 to process images. Here is the code for all the above stuff.

```python
from PIL import ImageGrab
import numpy as np
import cv2
while True:
    img = ImageGrab.grab(bbox(0,0,1280,720))
    img_np = np.array(img)
    cv2.imshow("Screen capture", img_np)
    cv2.waitkey(10)
```
When we launch this code. A pop window will appear and that means the screen capturing is started. We have an issue while capturing the screen which is a color issue. We will fix the color in the next step.

### Color Corrections

![image](https://cdn-images-1.medium.com/max/800/1*kzvx2P3JZ1TVVhgjdjdOXg.jpeg)

When we are capturing the images, it's exactly the RGB. Red-green-blue whatever is the color, it's not in the correct format so we will need to do a little bit of conversion.

So to do color convert we need to use `cv2.cvtColor(image_source, cv2.COLOR_BGR2RGB)`. This will take input as image as the first argument and convert it to RGB as the second argument.

Now your code will look like this.

```python
from PIL import ImageGrab
import numpy as np
import cv2
while True:
    img = ImageGrab.grab(bbox(0,0,1280,720))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen capture", img_final)
    cv2.waitkey(10)
```

### Make it fullscreen

As we can see from previous steps, our app is not capturing the full screen. So to make it full screen we need to install `win32api` package to get screen width and height dynamically. So to install this package, open your terminal and run the following line.

```bash
pip install pywin32
```

Now update the code.

```python
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# get system width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

while True:
    img = ImageGrab.grab(bbox(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen capture", img_final)
    cv2.waitkey(10)
```

### Saving The Recorded Video

![image](https://cdn-images-1.medium.com/max/800/1*mtJTAj7nzsUmR3mya1z_BA.jpeg)

To save video we need to use `cv2.VideoWriter_fourcc`.

```python
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter("output.mp4", fourcc, frame_rate (int), (width, height))
```
Now update your `main.py`

```python
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# get system width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# video encoding
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter("output.mp4", fourcc, frame_rate (int), (width, height))

while True:
    img = ImageGrab.grab(bbox(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen capture", img_final)
    captured_video.write(img_final)
    if cv2.waitkey(10) == ord('q'): # press q from your keyboard to stop recording
        break
```

Now, when you run this code it will store your recorded screen video as `output.mp4`. To stop recording please use `q` button from your keyboard.

### Give a dynamic filename
Now, I will give a dynamic to the output video with a timestamp. For that, we will need to use `datetime` package and update `main.py`.

```python
import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# get system width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# generate filename
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

# video encoding
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, frame_rate (int), (width, height))

while True:
    img = ImageGrab.grab(bbox(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen capture", img_final)
    captured_video.write(img_final)
    if cv2.waitkey(10) == ord('q'): # press q from your keyboard to stop recording
        break
```
### Capturing Webcam

![image](https://cdn-images-1.medium.com/max/800/1*A6w9QisFfdle-BCiiLsT4w.jpeg)

Opencv provides `cv2.VideoCapture(0)` method, which is used to capture the webcam.

```python
import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# get system width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# generate filename
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

# video encoding
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, frame_rate (int), (width, height))

# Capture webcam
webcam = cv2.VideoCapture(0)

while True:

    # pillow grab images
    img = ImageGrab.grab(bbox(0,0,width,height))

    # numpy array of images
    img_np = np.array(img)
    
    # color correction
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    
    # capture webcam
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    
    # cam window width and height
    img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]

    # open cv images
    cv2.imshow("Screen capture", img_final)
    
    # save video
    captured_video.write(img_final)
    
    if cv2.waitkey(10) == ord('q'): # press q from your keyboard to stop recording
        break
```

### Conclusion
So in this article on python programming, we have created a simple screen and webcam recording tool. And learned about some packages such as `pillow`, `numpy` and `opencv`. I hope this will help if you planning to create a screen capturing tool using python. and if you have any problem please feel free to ask. If you have any suggestions please leave a response below. Here is the [Source](https://www.youtube.com/watch?v=1J8dQA6gN7k) of this tutorial.

Thank you for reading this tutorial. Please follow me to read more articles like this.

You can also check out some cool articles here - 

[Make Your Own Chrome Browser with Python PyQt5](https://medium.com/p/make-your-own-chrome-browser-with-python-pyqt5-10b526dbc0a1)

[Create a Python-based Internet Speed Test GUI App: A Guide](https://medium.com/p/a-guide-to-python-internet-speed-test-gui-app-be2869f40036)

[Face Recognition in Under 25 Lines of Python Code](https://medium.com/p/face-recognition-under-25-lines-of-code-with-python-da7ccfe610c3)

[Python GUI Desktop App to Download YouTube Video — Python Coding](https://medium.com/p/python-gui-desktop-app-to-download-youtube-video-python-coding-5e1afe3f7f2c)
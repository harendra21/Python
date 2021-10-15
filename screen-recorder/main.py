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

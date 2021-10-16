# Automate WhatsApp messages with python

[Click here to read](https://medium.com/p/9c9d5cfad0d0)

![image](https://miro.medium.com/max/700/1*PCt4rZI7QSthzhwPF9H9pA.jpeg)

You can automate your WhatsApp message with just two lines of python code, and also you can schedule to send messages at midnight while you'll be sleeping. To automate your WhatsApp you to python installed in your system and any text editor or IDE (Integrated Development Kit). 

Sometimes we need to schedule and send messages at a particular time. Hence WhatsApp not providing this feature to schedule and message so, I think to provide the tutorial to solve this problem. This is very simple so let's get started.

### Install required packages

To automate WhatsApp you need to install `pywhatkit` package. This package is providing many awesome features with WhatsApp you can checkout [here](https://pypi.org/project/pywhatkit/). So to install `pywhatkit` open your terminal and run the following command:

```bash
pip install pywhatkit
```

Now you are ready to go.

### Send message with scheduling

![image](https://miro.medium.com/max/2400/1*lIrYErGPCTgfROqyaLJ7iw.jpeg)

To send a WhatsApp message with the schedule you have used the built-in method `sendwhatmsg(...)`.

#### The parameters are

- phone_num (required) - Phone number of the target with country code
- message (required) - Message that you want to sendwhatmsg
- time_hour (required) - Hours at which you want to send a message in 24-hour format
- time_min (required) - Minutes at which you want to send a message
- wait_time (optional, val = 20) - Seconds after which the message will be sent after opening the web
- print_wait_time (optional, val = True) - Will print the remaining time if set to true
- tab_close (optional, val = False) - True if you want to close the tab after sending the message

#### Example

```python
import pywhatkit as pwk

pwk.sendwhatmsg("+911212121212","This is test message", 12,14)

```

### Send image with caption

To send an image, Gif, or video with a caption we have to use `sendwhats_image(...)` method.

#### The parameters are
- phone_no (required) - Phone number of the target with country code
- img_path (required) - Path to image or gif or video
- caption (required) - The text that should appear below images
- wait_time (optional, val = 15) - Seconds after which the message will be sent after opening the web


#### Example

```python
import pywhatkit as pwk

pwk.sendwhats_image(phone_no="+911212121212",img_path="path_to_image",caption="This is test message")

```

### Conclusion

The `pywhatkit` is a very useful package especially when you want to automate WhatsApp messages this provides an easy way to solve your difficult problem and reduce code. This package also provides some other cool stuff like `playonyt(...)` play video on youtube, `search(...)` to search on google, `info(...)` to fetch information about any topic, `image_to_ascii_art(...)` to convert any image to ASCII art, `text_to_handwriting(...)` to convert text to handwriting format you can refer to [this link](https://pypi.org/project/pywhatkit/) to read everything in more details.

I hope you love this quick tutorial to "How you can automate WhatsApp message with python?". If you like this article please clap, and provide your response. Please follow me to get more tutorials like this.

*You can also check out some cool articles here -*

[How to create a screen and webcam recorder using python](https://medium.com/p/how-to-create-a-screen-and-webcam-recorder-using-python-21c407277d42)

[Make Your Own Chrome Browser with Python PyQt5](https://medium.com/p/make-your-own-chrome-browser-with-python-pyqt5-10b526dbc0a1)

[Create a Python-based Internet Speed Test GUI App: A Guide](https://medium.com/p/a-guide-to-python-internet-speed-test-gui-app-be2869f40036)

[Face Recognition in Under 25 Lines of Python Code](https://medium.com/p/face-recognition-under-25-lines-of-code-with-python-da7ccfe610c3)

[Python GUI Desktop App to Download YouTube Video — Python Coding](https://medium.com/p/python-gui-desktop-app-to-download-youtube-video-python-coding-5e1afe3f7f2c)
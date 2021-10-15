# Create a Python-based Internet Speed Test GUI App: A Guide

[Click here to read](https://medium.com/p/a-guide-to-python-internet-speed-test-gui-app-be2869f40036)

![image](https://miro.medium.com/max/1000/1*rw5i_RT5Rc5OasoWXeo1KA.jpeg)

Whenever we face an internet issue, the first thing we do is an internet speed test. So I have decided to create a Python app to check ping tests and your download speed. I have used pyspeedtest to use internet speed and Tkinter for GUI interface.
To use those packages in our application, first, we need to install them in our system. :)

### Install pyspeedtest

```bash
pip install pyspeedtest
```
### Install Tkinter in Ubuntu
```bash
sudo apt-get install python3-tk
```
To learn more about pyspeedtest, you can refer to the official documentation here.
### Testing pyspeedtest with terminal
#### Exploring options

![image](https://miro.medium.com/max/2400/1*7QJsPnmyTxHzEtzRAPXjOQ.png)

#### Check speed
```bash
$ pyspeedtest
Using server: speedtest.serv.pt
Ping: 9 ms
Download speed: 148.17 Mbps
Upload speed: 18.56 Mbps
```

#### Testing from a Python script:

```bash
>>> import pyspeedtest
>>> st = pyspeedtest.SpeedTest()
>>> st.ping()
9.306252002716064
>>> st.download()
42762976.92544772
>>> st.upload()
19425388.307319913
```

### Creating GUI app

Create speed-test.py file and paste the following code
```python
import pyspeedtest
from tkinter import *


def Speed_test():
	t = pyspeedtest.SpeedTest(e1.get())
	myping.set(t.ping())
	down.set(t.download())


master = Tk()
myping = StringVar()
down = StringVar()

Label(master, text="Website URL").grid(row=0, sticky=W)
Label(master, text="Ping Result:").grid(row=3, sticky=W)
Label(master, text="Download Result:").grid(row=4, sticky=W)

result = Label(master, text="", textvariable=myping,
			).grid(row=3, column=1, sticky=W)

result2 = Label(master, text="", textvariable=down,
				).grid(row=4, column=1, sticky=W)


e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Cheak", command=Speed_test)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
```

Done.

To run the following application, you need to run python3 speed-test.py. If python3 is not installed in your system, you need to install Python first. After running python3 speed-test.py, it will launch a GUI interface for the speed test.

![image](https://miro.medium.com/max/2400/1*m-ErpXzc9xVFdDMa3K_e0g.png)

Now you can enter server addresses such as www.google.com or www.youtube.com t and hit the check button to start testing your internet speed. It will show you ping speed in ms (milliseconds) and your download speed in bps (bits per second).

### Summary

So, in this Python app tutorial, we learned about pyspeedtest and Tkinter to create a GUI app. Tkinter is a widely used package to create GUI apps in python if you want to learn more about it in detail please refer to this link.

I hope it will help you to boost your knowledge and if you like this post please clap for it. It will motivate me to write more content. Thank you for reading.
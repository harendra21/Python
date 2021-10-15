# Make Your Own Chrome Browser with Python PyQt5
## How to create a simple web browser in Python?

[Click here to read](https://medium.com/p/make-your-own-chrome-browser-with-python-pyqt5-10b526dbc0a1)

![image](https://miro.medium.com/max/700/1*X7EyVEkGnHAXlgsWPFx6qw.png)

In this step-by-step Python coding tutorial, I will show you how to create a simple browser using the PyQt5 platform. The browser will allow us to open a URL in a window similar to chrome.

Python is an object-oriented programming language. The Qt library written in C++ is used for developing native desktop GUI applications and produces cross-platform code, so it’s a good tool to develop multi-platform applications. We can easily create our own web browser in Python with the help of the PyQT5 library and the version of Python 3 will suit well for this tutorial, though Python 2.7 is still in use in many organizations and in my environment also.

### Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/rMYnmcKXSlE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### PyQt5

Qt is a set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium-based web browser, as well as traditional UI development.

PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.

PyQt5 may also be embedded in C++based applications to allow users of those applications to configure or enhance the functionality of those applications. [source](https://pypi.org/project/PyQt5/)

### Package Installation
```bash
pip install PyQt5
pip install PyQtWebEngine
```

### I have generated a `requirements.txt` file to install required packages using pip.

```bash
PyQt5==5.15.4
PyQt5-Qt5==5.15.2
PyQt5-sip==12.9.0
PyQt5-stubs==5.15.2.0
PyQtWebEngine==5.15.4
PyQtWebEngine-Qt5==5.15.2
```

### Install requirements from requirements.txt
```bash
pip install -r requirements.txt
```

![image](https://miro.medium.com/max/2400/1*Tsf-cT3PLFVIBEuKIxgRwQ.png)

### Create Web Browser

TO create a web browser please follow the steps.

#### Import packages

```python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
```

#### Create main windows
```python
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # creating a QWebEngineView
        self.browser = QWebEngineView()

        # setting default browser url as google
        self.browser.setUrl(QUrl("http://google.com"))

        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding status bar to the main window
        self.setStatusBar(self.status)
```

#### Create PyQt Application
```python
# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Chrome Web Browser")

# creating a main window object
window = MainWindow()
```

### Run application
```python
# loop
app.exec_()
```

I have provided proper comments inside the coding part, it will automatically explain everything.
Here is the main.py file

```python
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # creating a QWebEngineView
        self.browser = QWebEngineView()

        # setting default browser url as google
        self.browser.setUrl(QUrl("http://google.com"))

        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding status bar to the main window
        self.setStatusBar(self.status)

        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")

        # adding this tool bar tot he main window
        self.addToolBar(navtb)

        # adding actions to the tool bar
        # creating a action for back
        back_btn = QAction("Back", self)

        # setting status tip
        back_btn.setStatusTip("Back to previous page")

        # adding action to the back button
        # making browser go back
        back_btn.triggered.connect(self.browser.back)

        # adding this action to tool bar
        navtb.addAction(back_btn)

        # similarly for forward action
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")

        # adding action to the next button
        # making browser go forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # similarly for home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # adding a separator in the tool bar
        navtb.addSeparator()

        # creating a line edit for the url
        self.urlbar = QLineEdit()

        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding this to the tool bar
        navtb.addWidget(self.urlbar)

        # adding stop action to the tool bar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # adding action to the stop button
        # making browser to stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # showing all the components
        self.show()

    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Geek Browser" % title)

    # method called by the home action
    def navigate_home(self):
        # open the google
        self.browser.setUrl(QUrl("http://www.google.com"))

    # method called by the line edit when return key is pressed
    def navigate_to_url(self):
        # getting url and converting it to QUrl object
        q = QUrl(self.urlbar.text())

        # if url is scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")

        # set the url to the browser
        self.browser.setUrl(q)

    # method for updating url
    # this method is called by the QWebEngineView object
    def update_urlbar(self, q):
        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Chrome Web Browser")

# creating a main window object
window = MainWindow()

# loop
app.exec_()
```

### Run you app

To run your app open terminal inside the root directory of your project and run -
python3 main.py

This will launch a web browser.

![image](https://miro.medium.com/max/700/1*WTblT_RrXO8eRqDYsFux1Q.png)

### Conclusion

I have covered all the basic things that are required to create a web browser using Python and PyQt5 library. I hope this will help you to build your awesome projects. You can add new features to it and send me in response. Please clap and follow me to read more articles like this. This article was inspired by this.
Thank you for reading!
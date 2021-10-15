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
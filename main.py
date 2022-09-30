from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

with open("test.xml") as fobj:
    data = fobj.read()

xml_data = BeautifulSoup(data, "xml")

def read_tags(file):
    for line in file:
        pass
        #print(line.get_text())

#raw_data = xml_data.find("body").get_text()


read_tags(xml_data)

root = Tk()
v = StringVar()
v.set("Hallo")
surname = Entry(root, textvariable=v).grid(row = 0, column = 0)



but = ttk.Button(root, text="Hilfe", command = lambda: print(v.get())).grid(row=0, column=1)

root.mainloop()
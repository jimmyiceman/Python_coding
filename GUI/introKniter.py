# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 01:05:05 2016
Obhjective: Introduction to Tkniter for GUI
@author: jatan.sharma
"""
'''
The tkinter module is a wrapper around tk, which is a wrapper around tcl, which is what is used to create windows and graphical user interfaces
The tkinter module's purpose is to generate GUIs. Python is not very popularly used for this purpose, but it is more than capable of doing it

'''


from tkinter import *

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master

# Root window created. Here, that would be the only window, but you can later have windows within windows     
root = Tk()

# Then we actually create the instance
app = Window(root)

# show it and begin the mainloop.
root.mainloop()
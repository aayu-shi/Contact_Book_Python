from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("About")
        self.geometry("650x450+600+200")
        self.resizable(False, False)

        # frames
        self.top = Frame(self, height=100, bg='#a5b5c4')
        self.top.pack(fill=X)

        # self.bottom = Frame(master, height=500, bg='#e9e3ff')
        self.bottom = Frame(self, height=350, bg='#e6e39c')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/about.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#a5b5c4')
        self.top_image_label.place(x=200, y=26)

        # heading
        self.heading = Label(self.top, text='About', font='times 18 bold', bg='#a5b5c4', fg='black')
        self.heading.place(x=280, y=40)

        self.text= Label(self.bottom, text='Hey! thank you for taking the time to go though my project\n This project '
                                           'was build as a part of my internship \n For any queries you can write me'
                                           ' at \n: ayushisharma89001@gmail.com', font='Sans 14 bold', bg='#e6e39c')
        self.text.place(x=40, y=100)



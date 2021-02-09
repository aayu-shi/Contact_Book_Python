from tkinter import *
from view import my_contacts
from add_contact import addContact
from about_us import About

class Application(object):
    def __init__(self, master):
        self.master = master

        # frames
        self.top = Frame(master, height=150, bg='#fce6e7')
        self.top.pack(fill=X)

        # self.bottom = Frame(master, height=500, bg='#e9e3ff')
        self.bottom = Frame(master, height=500, bg='#c5fcf0')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/agenda.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#fce6e7')
        self.top_image_label.place(x=160, y=40)

        # heading
        self.heading = Label(self.top, text='My Contact Book', font='times 22 bold', bg='#fce6e7', fg='black')
        self.heading.place(x=250, y=55)

        # button-view contacts
        self.view_button = Button(self.bottom, text='My Contacts', font='arial 12 bold', width='30',
                                  command=self.mycontacts)
        self.view_button.place(x=180, y=70)

        # button-add contacts
        self.view_button = Button(self.bottom, text='Add Contacts', font='arial 12 bold', width='30',
                                  command=self.addpeople)
        self.view_button.place(x=180, y=120)

        # button-delete contacts
        self.view_button = Button(self.bottom, text='About', font='arial 12 bold', width='30', command=self.about)
        self.view_button.place(x=180, y=170)


    def mycontacts(self):
        people = my_contacts()

    def addpeople(self):
        add = addContact()

    def about(self):
        about_page=About()



def main():
    root = Tk()
    app = Application(root)
    root.title("Contact Book")
    root.geometry("650x500+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
